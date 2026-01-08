#
#   Imports
#

from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

# Perso

from adapters.shared.dependencies import get_db_session, get_user
from adapters.features.categories.category_dto import CategoryRead
from adapters.features.categories.category_repo import CategoryRepo
from core.features.categories.category_service import CategoryService
from core.shared.models.user import User

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

    print(user)

    return categories