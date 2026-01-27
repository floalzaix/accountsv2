#
#   Imports
#

from pydantic import BaseModel
from typing import List

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
    child_rows: List["DetailsCategoryRowDTO"]

class DetailsTabDTO(BaseModel):
    """
        Represents a table of details per category of
        a transaction. Meant to be used in three cases
        scenarios:
        - Revenues details tab
        - Expenses details tab
        - Difference details tab
    """
    title_row: MonthlyValueDTO
    rows: List[DetailsCategoryRowDTO]
    total_row: MonthlyValueDTO
    