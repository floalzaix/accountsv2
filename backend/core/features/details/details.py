#
#   Imports
#

from dataclasses import dataclass, field
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
    rows: List[DetailsCategoryRow] = field(default_factory=list)
    total_row: MonthlyValue = field(default_factory=
        lambda: MonthlyValue(
            title="Total",
        )
    )

    #
    #   Methods
    #
    
    def append_row(self, row: DetailsCategoryRow) -> None:
        """
            Appends a row to the details table by summing the values
            of the row with the total row.
        """
        for key, value in row.values.__dict__.items():
            if key != "title" and isinstance(value, float):
                self.total_row.set_month_value_by_name(key, 
                    (self.total_row.get_month_value_by_name(key) or 0) + value
                )

        self.rows.append(row)

