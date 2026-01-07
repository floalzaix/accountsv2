#
#   Imports
#

import uuid

# Perso

from core.shared.ports.user_db_port import UserDBPort
from adapters.shared.utils.security_utils import hash_password, verify_password, verify_access_token
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

    async def login(
        self,
        *,
        email: str,
        password: str
    ) -> User:
        """
            Logs in a user.

            Verifies the password and returns the user.

            Params:
                - email: The email of the user.
                - password: The password of the user.

            Returns:
                - User: The user logged in.

            Raises:
                - ValueError: If the password is incorrect.
        """
        user = await self._user_db_port.by_email(email)

        if not verify_password(password, user.hash):
            raise ValueError("Invalid password")
            
        return user

    async def get_user_from_access_token(
        self,
        token: str
    ) -> User:
        """
            Gets a user from an access token.

            Returns the user if the token is valid.

            Raises:
                - ValueError: If the token is invalid.
                - ValueError: If the user is not found.
                - ValueError: If the token is expired.
        """
        user_id = int(verify_access_token(token))

        return await self._user_db_port.by_id(user_id)