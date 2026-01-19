#
#   Imports
#

import uuid

# Perso

from core.features.transactions.transaction import Transaction
from core.features.transactions.transactions_port import TransactionDBPort

#
#   Services
#

class TransactionsService:
    """
        Service for transactions.
    """
    def __init__(self, transaction_db_port: TransactionDBPort):
        self._transaction_db_port = transaction_db_port

    async def get_transactions(self, user_id: uuid.UUID) -> list[Transaction]:
        """
            Gets all transactions for a user.
        """
        return await self._transaction_db_port.get_transactions(user_id)

    async def create_transaction(self, transaction: Transaction) -> Transaction:
        """
            Creates a new transaction.
        """
        return await self._transaction_db_port.create_transaction(transaction)

    async def update_transaction(self, transaction: Transaction) -> Transaction:
        """
            Updates a transaction.
        """
        return await self._transaction_db_port.update_transaction(transaction)

    async def delete_transaction(self, transaction_id: uuid.UUID, user_id: uuid.UUID) -> None:
        """
            Deletes a transaction.
        """
        return await self._transaction_db_port.delete_transaction(transaction_id, user_id)