#
#   Imports
#

from enum import Enum

#
#   Enums
#

class DetailsTabType(str, Enum):
    REVENUES = "revenues"
    EXPENSES = "expenses"
    DIFFERENCES = "differences"