#
#   Imports
#

from dataclasses import dataclass
from typing import List

# Perso

from core.shared.models.monthly_value import MonthlyValue

#
#   Models
#

@dataclass
class DetailsCategoryRow:
    values: MonthlyValue
    child_rows: List["DetailsCategoryRow"]

@dataclass
class DetailsTab:
    """
        Represents a details table.
    """
    title_row: MonthlyValue
    rows: List[DetailsCategoryRow]
    total_row: MonthlyValue

