#
#   Imports
#

from dataclasses import dataclass
from typing import Any, Optional

#
#   Models
#

MONTHS = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december"
]

@dataclass
class MonthlyValue():
    """
        Represents a monthly value.

        For instance, you have a row of a table 
        that contains an amount oer month well, this class
        is used to validate the format of this row.

        Meant to be useed in the details tabs for example.
    """
    title: Optional[str] = None
    january: Optional[Any] = None
    february: Optional[Any] = None
    march: Optional[Any] = None
    april: Optional[Any] = None
    may: Optional[Any] = None
    june: Optional[Any] = None
    july: Optional[Any] = None
    august: Optional[Any] = None
    september: Optional[Any] = None
    october: Optional[Any] = None
    november: Optional[Any] = None  
    december: Optional[Any] = None
    
    #
    #   Properties
    #
    
    @property
    def total(self) -> Any:
        """
            Returns the total of the values.
        """
        s = 0

        for month in MONTHS:
            value = getattr(self, month)
            if isinstance(value, float):
                s += value

        return s

    #
    #   Methods
    #
    
    def set_month_value(self, month: int, value: Any) -> None:
        """
            Sets a value for a given month (number of the month).
        """
        setattr(self, MONTHS[int(month)], value)

    def set_month_value_by_name(self, month: str, value: Any) -> None:
        """
            Sets a value for a given month (name of the month).
        """
        setattr(self, month, value)