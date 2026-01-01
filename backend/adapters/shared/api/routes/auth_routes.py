#
#   Imports
#

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

# Perso

from adapters.shared.dependencies import get_db_session
from adapters.shared.validators.user_dto import (
    UserCreate, UserRead
)
from adapters.shared.db.repositories.user_repo import UserRepo

from core.shared.services.auth_service import AuthService


#
#   Routes
#

auth_routes = APIRouter()

@auth_routes.post(
    "/register",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
)
async def register(
    user_create: UserCreate,
    sb_session: AsyncSession = Depends(get_db_session),
):
    """
        Regsiters a new user using his email, password and pseudo.

        Params:
            - email: The email of the user.
            - password: The password of the user.
            - pseudo: The pseudo of the user (shorter name).

        Returns:
            - UserRead: The user created with its id, email,
            pseudo and status.
    """

    user_repo = UserRepo(session=sb_session)

    auth_service = AuthService(user_db_port=user_repo)

    try:
        created_user = await auth_service.register(
            id=user_create.id,
            email=user_create.email,
            password=user_create.password,
            pseudo=user_create.pseudo
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTPP_409_CONFLICT,
            detail={
                "user_safe_title": "User already exists",
                "user_safe_description": "The user with the "
                "given email already exists.",
                "dev": str(e)
            }
        )

    return created_user
