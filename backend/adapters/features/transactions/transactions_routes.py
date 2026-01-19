#
#   Imports
#

import uuid
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

# Perso

from adapters.shared.dependencies import get_db_session, get_user
from adapters.features.transactions.transactions_repo import TransactionsRepo
from core.features.transactions.transactions_service import TransactionsService
from adapters.features.transactions.transactions_dto import TransactionBase
from core.features.transactions.transaction import Transaction
from core.shared.models.user import User
from adapters.shared.utils.conversion_utils import pydantic_to_model

#
#   Routes
#

transactions_routes = APIRouter(prefix="/transactions")

@transactions_routes.get(
    "/",
    response_model=list[TransactionBase],
    status_code=status.HTTP_200_OK,
    summary="Get all transactions",
)
async def get_transactions(
    db_session: AsyncSession = Depends(get_db_session),
    user: User = Depends(get_user),
):
    """
        Gets all transactions for a user.
    """
    repo = TransactionsRepo(db_session)
    service = TransactionsService(repo)

    return await service.get_transactions(user.id)

@transactions_routes.post(
    "/",
    response_model=TransactionBase,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new transaction",
)
async def create_transaction(
    transaction: TransactionBase,
    db_session: AsyncSession = Depends(get_db_session),
    user: User = Depends(get_user),
):
    """
        Creates a new transaction for a user.
    """
    repo = TransactionsRepo(db_session)
    service = TransactionsService(repo)

    transaction.user_id = user.id

    transaction_model = pydantic_to_model(transaction, Transaction)

    try:
        created_transaction = await service.create_transaction(transaction_model)

        return created_transaction
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={
                "user_safe_title": "La transaction existe déjà",
                "user_safe_description": "La transaction avec les même "
                "date, motif, destinataire, catégories et montant "
                "existe déjà.",
                "dev": str(e)
            }
        )

@transactions_routes.put(
    "/",
    response_model=TransactionBase,
    status_code=status.HTTP_200_OK,
    summary="Update a transaction",
)
async def update_transaction(
    transaction: TransactionBase,
    db_session: AsyncSession = Depends(get_db_session),
    user: User = Depends(get_user),
):
    """
        Updates a transaction for a user.
    """
    repo = TransactionsRepo(db_session)
    service = TransactionsService(repo)

    transaction.user_id = user.id

    try:
        transaction_model = pydantic_to_model(transaction, Transaction)

        updated_transaction = await service.update_transaction(transaction_model)

        return updated_transaction
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={
                "user_safe_title": "La transaction existe déjà",
                "user_safe_description": "La transaction avec les même "
                "date, motif, destinataire, catégories et montant "
                "existe déjà.",
                "dev": str(e)
            }
        )

@transactions_routes.delete(
    "/{transaction_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a transaction",
)
async def delete_transaction(
    transaction_id: uuid.UUID,
    db_session: AsyncSession = Depends(get_db_session),
    user: User = Depends(get_user),
):
    """
        Deletes a transaction for a user.
    """

    repo = TransactionsRepo(db_session)
    service = TransactionsService(repo)

    return await service.delete_transaction(transaction_id, user.id)