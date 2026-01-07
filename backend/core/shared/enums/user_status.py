#
#   Imports
#

from enum import Enum

#
#   Enums
#

class UserStatus(str, Enum):
    ACTIVE = "active"
    DELETED = "deleted"