#
#   Imports
#

from pydantic import BaseModel, Field
from typing import Any, Optional

#
#   DTOs
#

class MonthlyValueDTO(BaseModel):
    """
        Base model for a monthly value.

        For instance, you have a row of a table 
        that contains an amount oer month well, this DTO
        is used to validate the format of this row.

        Meant to be useed in the details tabs fo example.
    """
    title: str = Field(
        description="The title of the monthly value"
    )
    january: Any = Field(
        description="The monthly value for January"
    )
    february: Any = Field(
        description="The monthly value for February"
    )
    march: Any = Field(
        description="The monthly value for March"
    )
    april: Any = Field(
        description="The monthly value for April"
    )
    may: Any = Field(
        description="The monthly value for May"
    )
    june: Any = Field(
        description="The monthly value for June"
    )
    july: Any = Field(
        description="The monthly value for July"
    )
    august: Any = Field(
        description="The monthly value for August"
    )
    september: Any = Field(
        description="The monthly value for September"
    )
    october: Any = Field(
        description="The monthly value for October"
    )
    november: Any = Field(
        description="The monthly value for November"
    )
    december: Any = Field(
        description="The monthly value for December"
    )
    total: Optional[Any] = Field(
        description="The total value"
    )