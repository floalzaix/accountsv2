#
#   Imports
#

import uuid
from typing import cast

from sqlalchemy import extract, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

# Perso

from adapters.features.transactions.transactions_orm import TransactionORM
from core.features.transactions.transactions_port import TransactionDBPort
from core.features.transactions.transaction import Transaction
from adapters.shared.utils.conversion_utils import orm_to_model, model_to_orm
from adapters.features.categories.category_orm import CategoryORM

#
#   Repositories
#

class TransactionsRepo(TransactionDBPort):
    """
        Repository for transactions operations.
    """
    def __init__(self, session: AsyncSession):
        self.session = session

    async def by_id(
        self,
        transaction_id: uuid.UUID,
        user_id: uuid.UUID
    ) -> Transaction:
        query = (
            select(TransactionORM)
            .where(TransactionORM.id == transaction_id)
            .where(TransactionORM.user_id == user_id)
        )

        result = await self.session.execute(query)

        transaction_orm = result.scalar_one_or_none()

        if transaction_orm is None:
            raise ValueError(f"Transaction with id {transaction_id} "
            f"and user id {user_id} not found !")
    
        return orm_to_model(transaction_orm, Transaction)

    async def get_transactions(self, user_id: uuid.UUID, trans_type: str, year: int) -> list[Transaction]:
        year_column = extract('year', TransactionORM.event_date)

        query = (
            select(TransactionORM)
            .where(TransactionORM.user_id == user_id)
            .where(TransactionORM.type == trans_type)
            .where(year_column == year)
        )
        result = await self.session.execute(query)
        transactions_orm = result.scalars().all()
        return [
            orm_to_model(transaction_orm, Transaction) 
            for transaction_orm in transactions_orm
        ]

    async def _verify_unique_transaction(
        self, transaction: TransactionORM) -> None:
        """
            Verifies if a transaction is unique meaning it
            is not a duplicate to avoid mistakes for the user.

            Params:
                - transaction: The transaction to verify.

            Raises:
                - ValueError: If the transaction already exists.
        """
        query = (
            select(TransactionORM)
            .where(TransactionORM.event_date == transaction.event_date)
            .where(TransactionORM.motive == transaction.motive)
            .where(TransactionORM.to == transaction.to)
            .where(TransactionORM.bank_date == transaction.bank_date)
            .where(TransactionORM.type == transaction.type)
            .where(TransactionORM.amount == transaction.amount)
            .where(TransactionORM.user_id == transaction.user_id)
            .where(TransactionORM.category1_id == transaction.category1_id)
            .where(TransactionORM.category2_id == transaction.category2_id)
            .where(TransactionORM.category3_id == transaction.category3_id)
        )

        result = await self.session.execute(query)
        if result.scalars().first() is not None:
            raise ValueError("Transaction already exists !")

    async def _verify_category(
        self,
        category_id: uuid.UUID,
        level: int,
        user_id: uuid.UUID,
        parent_id: uuid.UUID | None = None
    ) -> None:
        """
            Verifies if a category exists and if the level is correct
            finally checks if the parent id is correct.

            Params:
                - category_id: The id of the category to verify.
                - level: The level of the category to verify.
                - user_id: The id of the user who made the transaction.

            Raises:
                - RuntimeError: If the category does not exist or the level is not correct.
        """
        
        query = (
            select(CategoryORM)
            .where(CategoryORM.id == category_id)
            .where(CategoryORM.level == level)
        )

        result = await self.session.execute(query)
        category_orm = result.scalar_one_or_none()

        if category_orm is None:
            raise RuntimeError(f"Category with id {category_id} and "
            f"user_id {user_id} and level {level} not found !")

        if category_orm.level != level:
            raise RuntimeError("Levels not matching !")

        if parent_id is not None and category_orm.parent_id != parent_id:
            raise ValueError("Parent id not matching !")

    async def _verify_categories(self, transaction: Transaction) -> None:
        """
            Verifies if the categories exist and if the levels are correct.

            Params:
                - transaction: The transaction to verify.

            Raises:
                - RuntimeError: If the categories do not exist or the levels are not correct.
        """
        if transaction.category1_id is not None:
            await self._verify_category(transaction.category1_id, 0, transaction.user_id)

        if transaction.category2_id is not None:
            if transaction.category1_id is None:
                raise ValueError("Category 1 id is required for category 2 !")
            await self._verify_category(transaction.category2_id, 1, transaction.user_id, transaction.category1_id)

        if transaction.category3_id is not None:
            if transaction.category2_id is None:
                raise ValueError("Category 2 id is required for category 3 !")
            await self._verify_category(transaction.category3_id, 2, transaction.user_id, transaction.category2_id)

    async def create_transaction(self, transaction: Transaction) -> Transaction:
        transaction_orm = cast(
            TransactionORM, model_to_orm(transaction, TransactionORM)
        )

        await self._verify_unique_transaction(transaction_orm)
        await self._verify_categories(transaction)

        self.session.add(transaction_orm)
        await self.session.commit()

        return transaction

    async def update_transaction(self, transaction: Transaction) -> Transaction:
        transaction_orm = cast(
            TransactionORM, model_to_orm(transaction, TransactionORM)
        )

        await self._verify_unique_transaction(transaction_orm)
        await self._verify_categories(transaction)

        query = (
            update(TransactionORM)
            .where(TransactionORM.id == transaction.id)
            .values({
                "event_date": transaction.event_date,
                "motive": transaction.motive,
                "to": transaction.to,
                "bank_date": transaction.bank_date,
                "type": transaction.type,
                "amount": transaction.amount,
                "category1_id": transaction.category1_id,
                "category2_id": transaction.category2_id,
                "category3_id": transaction.category3_id,
            })
        )

        result = await self.session.execute(query)
        await self.session.commit()

        # Verifying if the transaction exists
        if (result.rowcount <= 0): # type: ignore
            raise RuntimeError(f"Transaction with id {transaction.id} "
            f"and user id {transaction.user_id} not found !")

        return transaction

    async def delete_transaction(self, transaction_id: uuid.UUID, user_id: uuid.UUID) -> None:
        query = (
            delete(TransactionORM)
            .where(TransactionORM.id == transaction_id)
            .where(TransactionORM.user_id == user_id)
        )

        result = await self.session.execute(query)
        await self.session.commit()

        # Verifying if the category was deleted
        if (result.rowcount <= 0): # type: ignore
            raise RuntimeError(f"Transaction with id {transaction_id} "
            f"and user id {user_id} not found !")