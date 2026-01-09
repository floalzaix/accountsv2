#
#   Imports
#

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

# Perso

from adapters.shared.dependencies import get_db_session
from adapters.shared.validators.user_dto import (
    UserCreate, UserLogin, UserRead, UserBearer
)
from adapters.shared.db.repositories.user_repo import UserRepo
from adapters.shared.utils.security_utils import create_access_token
from core.shared.services.auth_service import AuthService
from core.shared.models.user import User
from adapters.shared.dependencies import get_user

#
#   Routes
#

auth_routes = APIRouter(prefix="/auth")

@auth_routes.post(
    "/register",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
)
async def register(
    user_create: UserCreate,
    db_session: AsyncSession = Depends(get_db_session),
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

    user_repo = UserRepo(session=db_session)

    auth_service = AuthService(user_db_port=user_repo)

    try:
        created_user = await auth_service.register(
            id=user_create.id,
            email=user_create.email,
            password=user_create.password,
            pseudo=user_create.pseudo
        )

        return created_user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={
                "user_safe_title": "L'utilisateur existe déjà",
                "user_safe_description": "L'utilisateur avec l'email "
                "donné existe déjà.",
                "dev": str(e)
            }
        )

@auth_routes.post(
    "/login",
    response_model=UserBearer,
    status_code=status.HTTP_200_OK,
    summary="Login a user",
)
async def login(
    user_login: UserLogin,
    sb_session: AsyncSession = Depends(get_db_session),
):
    """
        Logs in a user using his email and password.

        Params:
            - email: The email of the user.
            - password: The password of the user.

        Returns:
            - dict: The access token, the user and the token type.

        Raises:
            - ValueError: If the password is incorrect.
    """
    try:
        user_repo = UserRepo(session=sb_session)
        auth_service = AuthService(user_db_port=user_repo)

        logged_user = await auth_service.login(
            email=user_login.email,
            password=user_login.password
        )

        access_token = create_access_token(logged_user.id)

        return {
            "access_token": access_token,
            "user": logged_user,
            "token_type": "Bearer"
        }
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={
                "user_safe_title": "Mot de passe et/ou email incorrect",
                "user_safe_description": "Le mot de passe donné est incorrect.",
                "dev": str(e)
            }
        )

@auth_routes.get(
    "/me",
    response_model=UserRead,
    status_code=status.HTTP_200_OK,
    summary="Get the current user",
)
async def me(
    user: User = Depends(get_user),
):
    """
        Gets the current user from the database.

        It is a mean to verify if authenticated for the frontend
        for exemple.
    """
    return user