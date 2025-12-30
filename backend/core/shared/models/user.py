#
#   Imports
#

from typing import Optional
from core.shared.enums.user_status import UserStatus

#
#   Models
#

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
    def __init__(
        self,
        *,
        id: Optional[int] = None,
        email: Optional[str] = None,
        hash: Optional[str] = None,
        pseudo: Optional[str] = None,
        status: Optional[UserStatus] = None
    ):
        self.id = id
        self.email = email
        self.hash = hash
        self.pseudo = pseudo
        self.status = status