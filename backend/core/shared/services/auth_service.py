#
#   Imports
#

import uuid

# Perso

from core.shared.ports.user_db_port import UserDBPort
from adapters.shared.utils.security_utils import hash_password
from core.shared.models.user import User
from core.shared.enums.user_status import UserStatus

#
#   Services
#

class AuthService:
    """
        Service for authentication and authorization.

        Connects the user to the app using the database data.
    """
    def __init__(self, user_db_port: UserDBPort):
        self._user_db_port = user_db_port

    async def register(
        self,
        *,
        id: uuid.UUID,
        email: str,
        password: str,
        pseudo: str
    ) -> User:
        """
            Registers a new user.

            Hashes the password and creates the user in the 
            db through the port.
        """

        # Hashing password
        hash = hash_password(password)

        # Creating user
        user = User(
            id=id,
            email=email,
            hash=hash,
            pseudo=pseudo,
            status=UserStatus.ACTIVE
        )
        await self._user_db_port.create_user(user)

        return user