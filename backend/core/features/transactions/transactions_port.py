#
#   Imports
#

import uuid
from abc import ABC, abstractmethod

# Perso

from core.features.transactions.transaction import Transaction

#
#   Ports
#

class TransactionDBPort(ABC):
    @abstractmethod
    async def by_id(self, transaction_id: uuid.UUID, user_id: uuid.UUID) -> Transaction:
        """
            Gets a transaction by id.

            Params:
                - transaction_id: The id of the transaction to get.
                - user_id: The id of the user who made the transaction.

            Returns:
                - The transaction.

            Raises:
                - ValueError: If the transaction does not exist.
        """
        pass

    @abstractmethod
    async def get_transactions(self, user_id: uuid.UUID, trans_type: str) -> list[Transaction]:
        """
            Gets all transactions for a user. It can be filtered by
            transaction type meaning which accounts is targeted.

            If there are no transactions, returns an empty list.
        """
        pass

    @abstractmethod
    async def create_transaction(self, transaction: Transaction) -> Transaction:
        """
            Creates a new transaction for a user.

            Params:
                - transaction: The transaction to create.
                - user_id: The id of the user who made the transaction.

            Returns:
                - The created transaction.

            Raises:
                - ValueError: If the transaction already exists.
                - RuntimeError: If the categories do not exist or the levels are not correct.
        """
        pass

    @abstractmethod
    async def update_transaction(self, transaction: Transaction) -> Transaction:
        """
            Updates a transaction for a user.

            Params:
                - transaction: The transaction to update.
                - user_id: The id of the user who made the transaction.

            Returns:
                - The updated transaction.

            Raises:
                - RuntimeError: If the transaction does not exist.
                - ValueError: If the transaction already exists.
                - RuntimeError: If the categories do not exist or the levels are not correct.
        """
        pass

    @abstractmethod
    async def delete_transaction(self, transaction_id: uuid.UUID, user_id: uuid.UUID) -> None:
        """
            Deletes a transaction for a user.

            Params:
                - transaction_id: The id of the transaction to delete.
                - user_id: The id of the user who made the transaction.

            Raises:
                - RuntimeError: If the transaction does not exist.
        """
        pass