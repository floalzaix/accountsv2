#
#   Imports
#

import uuid

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, extract

# Perso

from core.features.summary.summary_port import SummaryDBPort
from core.shared.enums.trans_type import TransType
from adapters.features.transactions.transactions_orm import TransactionORM
#
#   Repositories
#

class SummaryRepo(SummaryDBPort):
    """
        Repository for summary operations.
    """
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_balance(
        self,
        user_id: uuid.UUID,
        year: int,
        trans_types: list[TransType]
    ) -> float:
        """
            Gets the balance of the user. For a year and
            depending on the transactions types selected.
        """

        year_extracted = extract('year', TransactionORM.event_date)
        
        query = (
            select(func.sum(TransactionORM.amount))
            .where(
                TransactionORM.user_id == user_id,
                year_extracted == year,
                TransactionORM.type.in_(trans_types)
            )
        )

        result = await self.session.execute(query)

        amount = result.scalar_one_or_none()
        if amount is None:
            return 0.0
            
        return amount