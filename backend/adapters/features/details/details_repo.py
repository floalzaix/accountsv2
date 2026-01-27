#
#   Imports
#

import uuid

from enum import Enum
from sqlalchemy import extract, func, or_, select
from sqlalchemy.ext.asyncio import AsyncSession

# Perso

from adapters.features.details.details_dto import DetailsTabDTO
from adapters.features.transactions.transactions_orm import TransactionORM
from backend.adapters.features.categories.category_orm import CategoryORM

#
#   Repositories
#

class DetailsTabType(str, Enum):
    REVENUES = "revenues"
    EXPENSES = "expenses"
    DIFFERENCES = "differences"

class DetailsRepo:
    """
        Repository for details operations.
    """
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_detailed_tab(
        self,
        year: int,
        trans_type: str,
        user_id: uuid.UUID,
        tab_type: DetailsTabType
    ) -> None:
        trans_month = extract("month", TransactionORM.event_date)

        query = (
            select(
                CategoryORM.id,
                trans_month,
                func.sum(TransactionORM.amount)
            )
            .join(TransactionORM, or_(
                    CategoryORM.id == TransactionORM.category1_id,
                    CategoryORM.id == TransactionORM.category2_id,
                    CategoryORM.id == TransactionORM.category3_id,
                )
            )
            .where(TransactionORM.user_id == user_id)
            .where(extract("year", TransactionORM.event_date) == year)
            .where(TransactionORM.type == trans_type)
            .group_by(trans_month, CategoryORM.id)
        )

        result = await self.session.execute(query)

        rows = result.all()

        print(rows)