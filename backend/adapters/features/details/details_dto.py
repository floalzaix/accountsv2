#
#   Imports
#

from pydantic import BaseModel
from typing import List, Optional

# Perso

from adapters.shared.validators.monthly_value_dto import MonthlyValueDTO

#
#   DTOs
#

class DetailsCategoryRowDTO(BaseModel):
    """
        Represents a row of a category in the details table.
    """
    values: MonthlyValueDTO
    child_rows: Optional[List["DetailsCategoryRowDTO"]] = None

class DetailsTabDTO(BaseModel):
    """
        Represents a table of details per category of
        a transaction. Meant to be used in three cases
        scenarios:
        - Revenues details tab
        - Expenses details tab
        - Difference details tab
    """
    rows: List[DetailsCategoryRowDTO]
    total_row: MonthlyValueDTO
    