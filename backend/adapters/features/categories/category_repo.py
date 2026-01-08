#
#   Imports
#

import uuid

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from typing import List

# Perso

from core.features.categories.category_port import CategoryDBPort
from core.features.categories.category import Category
from adapters.features.categories.category_orm import CategoryORM
from adapters.shared.utils.conversion_utils import orm_to_model

#
#   Repositories
#

class CategoryRepo(CategoryDBPort):
    """
        Repository for category operations.
    """
    def __init__(self, session: AsyncSession):
        self._session = session

    async def by_id(self, category_id: uuid.UUID) -> Category:
        query = select(CategoryORM).where(CategoryORM.id == category_id)

        result = await self._session.execute(query)

        category_orm = result.scalar_one_or_none()

        if category_orm is None:
            raise ValueError(f"Category with id {category_id} not found")

        return orm_to_model(category_orm, Category)

    async def by_user_id(self, user_id: uuid.UUID) -> List[Category]:
        query = (
            select(CategoryORM)
            .where(CategoryORM.user_id == user_id)
            .options(selectinload(CategoryORM.parents))
        )

        result = await self._session.execute(query)

        categories = result.scalars().all()

        category_models: List[Category] = [
            orm_to_model(cat, Category)
            for cat in categories
        ]

        return category_models

