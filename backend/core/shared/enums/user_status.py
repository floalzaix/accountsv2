#
#   Imports
#

from enum import Enum

#
#   Enums
#

class UserStatus(Enum, str):
    ACTIVE = "active"
    DELETED = "deleted"