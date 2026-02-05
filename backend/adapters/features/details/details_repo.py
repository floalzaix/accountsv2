#
#   Imports
#

import uuid

from typing import Any, Dict, List
from sqlalchemy import extract, func, or_, select
from sqlalchemy.ext.asyncio import AsyncSession

# Perso

from adapters.features.transactions.transactions_orm import TransactionORM
from adapters.features.categories.category_orm import CategoryORM
from core.features.details.details_port import DetailsDBPort
from core.shared.enums.details_tab_type import DetailsTabType
from core.shared.models.monthly_value import MonthlyValue
from core.features.details.details import DetailsCategoryRow, DetailsTab
from core.features.categories.category import Category

#
#   Repositories
#

class DetailsRepo(DetailsDBPort):
    """
        Repository for details operations.
    """
    def __init__(self, session: AsyncSession):
        self.session = session

    async def _get_other_category(
        self,
        user_id: uuid.UUID,
        year: int,
        trans_type: str,
        tab_type: DetailsTabType
    ) -> List[Any]:
        """
            Gets the other category when they don't have a category.
        """
        trans_month = extract("month", TransactionORM.event_date)

        # Fetching the final row the other transactions with no category
        query = (
            select(
                trans_month,
                func.sum(TransactionORM.amount)
            )
            .where(TransactionORM.user_id == user_id)
            .where(extract("year", TransactionORM.event_date) == year)
            .where(TransactionORM.type == trans_type)
            .where(
                TransactionORM.amount > 0 if tab_type == DetailsTabType.REVENUES else
                TransactionORM.amount < 0 if tab_type == DetailsTabType.EXPENSES else
                TransactionORM.amount != 0
            )
            .where(TransactionORM.category1_id.is_(None))
            .where(TransactionORM.category2_id.is_(None))
            .where(TransactionORM.category3_id.is_(None))
            .group_by(trans_month)
        )

        result = await self.session.execute(query)
        other_row = result.all()

        # Faking the other category
        other_row = [(Category(
            id=uuid.uuid4(),
            name="Other",
            parent_id=None,
            level=0,
            user_id=user_id
        ), month_number, sum) for month_number, sum in other_row]

        return other_row

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

        cat_rows = result.all()

        other_row = await self._get_other_category(user_id, year, trans_type, tab_type)

        # Mergin the category rows and the other row
        db_rows: List[Any] = [*cat_rows, *other_row]

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