#
#   Imports
#

from dataclasses import dataclass
from typing import List, Optional

# Perso

from core.shared.models.monthly_value import MonthlyValue

#
#   Models
#

@dataclass
class DetailsCategoryRow:
    values: MonthlyValue
    child_rows: Optional[List["DetailsCategoryRow"]] = None

@dataclass
class DetailsTab:
    """
        Represents a details table.
    """
    rows: List[DetailsCategoryRow]
    total_row: MonthlyValue = MonthlyValue(
        title="Total",
    )

    #
    #   Methods
    #
    
    def append_row(self, row: DetailsCategoryRow) -> None:

        self.rows.append(row)

