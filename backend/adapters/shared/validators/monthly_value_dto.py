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
    title: Optional[str] = Field(
        default=None,
        description="The title of the monthly value"
    )
    january: Optional[Any] = Field(
        default=None,
        description="The monthly value for January"
    )
    february: Optional[Any] = Field(
        default=None,
        description="The monthly value for February"
    )
    march: Optional[Any] = Field(
        default=None,
        description="The monthly value for March"
    )
    april: Optional[Any] = Field(
        default=None,
        description="The monthly value for April"
    )
    may: Optional[Any] = Field(
        default=None,
        description="The monthly value for May"
    )
    june: Optional[Any] = Field(
        default=None,
        description="The monthly value for June"
    )
    july: Optional[Any] = Field(
        default=None,
        description="The monthly value for July"
    )
    august: Optional[Any] = Field(
        default=None,
        description="The monthly value for August"
    )
    september: Optional[Any] = Field(
        default=None,
        description="The monthly value for September"
    )
    october: Optional[Any] = Field(
        default=None,
        description="The monthly value for October"
    )
    november: Optional[Any] = Field(
        default=None,
        description="The monthly value for November"
    )
    december: Optional[Any] = Field(
        default=None,
        description="The monthly value for December"
    )
    total: Optional[Any] = Field(
        default=None,
        description="The total value"
    )