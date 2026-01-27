#
#   Imports
#

from dataclasses import dataclass
from typing import Any, Optional

#
#   Models
#

@dataclass
class MonthlyValue():
    """
        Represents a monthly value.

        For instance, you have a row of a table 
        that contains an amount oer month well, this class
        is used to validate the format of this row.

        Meant to be useed in the details tabs for example.
    """
    title: str
    january: Any
    february: Any
    march: Any
    april: Any
    may: Any
    june: Any
    july: Any
    august: Any
    september: Any
    october: Any
    november: Any
    december: Any
    total: Optional[Any] = None