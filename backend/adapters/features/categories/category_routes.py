#
#   Imports
#

import uuid

from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

# Perso

from adapters.shared.dependencies import get_db_session, get_user
from adapters.features.categories.category_dto import CategoryRead, CategoryCreate, CategoryUpdate
from adapters.features.categories.category_repo import CategoryRepo
from core.features.categories.category_service import CategoryService
from core.shared.models.user import User
from adapters.shared.utils.conversion_utils import pydantic_to_model
from core.features.categories.category import Category

#
#   Routes
#

category_routes = APIRouter(prefix="/categories")

@category_routes.get(
    "/",
    response_model=List[CategoryRead],
    status_code=status.HTTP_200_OK,
    summary="List all categories for a given user",
)
async def list_categories(
    user: User = Depends(get_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
        List all categories for a given user.
    """
    category_repo = CategoryRepo(session=db_session)

    category_service = CategoryService(category_db_port=category_repo)

    categories = await category_service.list_categories(user_id=user.id)

    return categories

@category_routes.post(
    "/",
    response_model=CategoryRead,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new category for a given user",
)
async def create_category(
    category_create: CategoryCreate,
    user: User = Depends(get_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
        Create a new category for a given user.
    """
    category_repo = CategoryRepo(session=db_session)

    category_service = CategoryService(category_db_port=category_repo)

    category_create.user_id = user.id

    category_model: Category = pydantic_to_model(category_create, Category)

    try:
        category = await category_service.create_category(category_model)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={
                "user_safe_title": "Catégorie déjà existante",
                "user_safe_description": "La catégorie existe probablement déjà.",
                "dev": str(e)
            }
        )

    return category

@category_routes.put(
    "/{category_id}",
    response_model=CategoryRead,
    status_code=status.HTTP_200_OK,
    summary="Update a category for a given user",
)
async def update_category(
    category_id: uuid.UUID,
    category_update: CategoryUpdate,
    user: User = Depends(get_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    """
        Update a category for a given user.
    """
    category_repo = CategoryRepo(session=db_session)

    category_service = CategoryService(category_db_port=category_repo)

    try:
        category = await category_service.update_category(
            category_id=category_id,
            user_id=user.id,
            name=category_update.name
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={
                "user_safe_title": "Catégorie non trouvée ou nom déjà "
                "utilisé",
                "user_safe_description": "La catégorie avec l'id donné "
                "n'existe pas ou le nom donné est déjà utilisé.",
                "dev": str(e)
            }
        )

    return category
    