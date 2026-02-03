#
#   Imports
#

import uuid

from typing import Dict
from sqlalchemy import extract, func, or_, select
from sqlalchemy.ext.asyncio import AsyncSession

# Perso

from adapters.features.transactions.transactions_orm import TransactionORM
from adapters.features.categories.category_orm import CategoryORM
from core.features.details.details_port import DetailsDBPort
from core.shared.enums.details_tab_type import DetailsTabType
from core.shared.models.monthly_value import MonthlyValue
from core.features.details.details import DetailsCategoryRow, DetailsTab

#
#   Repositories
#

class DetailsRepo(DetailsDBPort):
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
    ) -> DetailsTab:
        #
        #   Query to get the data from the category
        #
        trans_month = extract("month", TransactionORM.event_date)

        query = (
            select(
                CategoryORM,
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
            .where(
                TransactionORM.amount > 0 if tab_type == DetailsTabType.REVENUES else
                TransactionORM.amount < 0 if tab_type == DetailsTabType.EXPENSES else
                TransactionORM.amount != 0
            )
            .group_by(trans_month, CategoryORM.id)
            .order_by(CategoryORM.name)
        )

        result = await self.session.execute(query)

        db_rows = result.all()

        #
        #   Process the data
        #

        # Creating the tab rows
        tab_rows: Dict[str, DetailsCategoryRow] = {}
        parent_dict: Dict[str, str] = {}
        for cat, month_number, sum in db_rows:
            if cat.id not in tab_rows:
                tab_rows[cat.id] = DetailsCategoryRow(
                    values=MonthlyValue(
                        title=cat.name,
                    )
                )

            # Create the pairing between the category and its parent
            if cat.parent_id is not None:
                parent_dict[cat.id] = cat.parent_id

            tab_rows[cat.id].values.set_month_value(month_number, sum)

        # Creating the list and apply hierarchy
        details_tab = DetailsTab()
        for cat_id, row in tab_rows.items():

            # If the category has no parent, add it to the list
            # as a root category
            if cat_id not in parent_dict:
                details_tab.append_row(row)

            # If the category has a parent, add it to the parent's child rows
            else:
                parent_id = parent_dict[cat_id]
                parent_row = tab_rows[parent_id]

                # If the parent row has no child rows, create a new list
                if parent_row.child_rows is None:
                    parent_row.child_rows = []

                parent_row.child_rows.append(row)

        return details_tab