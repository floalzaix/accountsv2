#
#   Imports
#

from enum import Enum

#
#   Enums
#

class TransType(str, Enum):
    """
        Type of transaction.
    """
    CHECKING = "checking"
    SAVINGS = "savings"
    CASH = "cash"