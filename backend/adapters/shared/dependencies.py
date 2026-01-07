#
#   Imports
#

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

# Perso

from adapters.shared.db.bootstrap import get_session
from adapters.shared.db.repositories.user_repo import UserRepo
from core.shared.services.auth_service import AuthService

#
#   Dependancies
#

async def get_db_session(
    session: AsyncSession = Depends(get_session)
) -> AsyncSession:
    return session

async def get_user(
    token: str = Depends(OAuth2PasswordBearer(tokenUrl="auth/login")),
    session: AsyncSession = Depends(get_db_session)
):
    """
        Gets a user from an access token.

        Params:
            - token: The access token.
            - session: The database session.

        Returns:
            - User: The user.

        Raises:
            - ValueError: If the user is not found.
            - ValueError: If the token is invalid.
            - ValueError: If the token is expired.
    """
    repo = UserRepo(session=session)
    auth_service = AuthService(user_db_port=repo)

    user = await auth_service.get_user_from_access_token(token=token)

    return user