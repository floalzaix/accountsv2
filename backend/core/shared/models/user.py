#
#   Imports
#

import uuid
from dataclasses import dataclass

# Perso

from core.shared.enums.user_status import UserStatus

#
#   Models
#

@dataclass
class User:
    """
        Reprensents a user.

        Attributes:
            - id: The user's id.
            - email: The user's email.
            - hash: The user's password hash.
            - pseudo: The user's nickname.
            - status: The user's status (to avoid having to delete
            the user from the database).
    """
    id: uuid.UUID
    email: str
    hash: str
    pseudo: str
    status: UserStatus