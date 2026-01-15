#
#   Imports
#

import uuid

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from typing import List

# Perso

from core.features.categories.category_port import CategoryDBPort
from core.features.categories.category import Category
from adapters.features.categories.category_orm import CategoryORM
from adapters.shared.utils.conversion_utils import model_to_orm, orm_to_model

#
#   Repositories
#

class CategoryRepo(CategoryDBPort):
    """
        Repository for category operations.
    """
    def __init__(self, session: AsyncSession):
        self._session = session

    async def by_id(self, category_id: uuid.UUID, user_id: uuid.UUID) -> Category:
        query = (
            select(CategoryORM)
            .where(CategoryORM.id == category_id)
            .where(CategoryORM.user_id == user_id)
        )

        result = await self._session.execute(query)

        category_orm = result.scalar_one_or_none()

        if category_orm is None:
            raise ValueError(f"Category with id {category_id} not found")

        return orm_to_model(
            category_orm,
            Category,
        )

    async def by_name(self, name: str, user_id: uuid.UUID) -> List[Category]:
        query = (
            select(CategoryORM)
            .where(CategoryORM.name == name)
            .where(CategoryORM.user_id == user_id)
        )

        result = await self._session.execute(query)

        category_orms = result.scalars().all()
        
        if len(category_orms) == 0:
            raise ValueError(f"No categories with name {name} "
            f"found for user {user_id}.")

        return [orm_to_model(
            category_orm,
            Category,
        ) for category_orm in category_orms]

    async def by_user_id(self, user_id: uuid.UUID) -> List[Category]:
        query = (
            select(CategoryORM)
            .where(CategoryORM.user_id == user_id)
        )

        result = await self._session.execute(query)

        categories = result.scalars().all()

        category_models: List[Category] = [
            orm_to_model(
                cat,
                Category,
            )
            for cat in categories
        ]

        return category_models
    
    async def _verify_uq_name_parent(
        self,
        name: str,
        parent_id: uuid.UUID,
        user_id: uuid.UUID
    ) -> None:
        """
            Verifies if the name is already in use for the same parent.

            Params:
                - name: The name of the category to verify.
                - parent_id: The parent id of the category to verify.
                - user_id: The user id of the category to verify.

            Raises:
                - ValueError: If the name is already in use for the same parent.
        """
        try:
            categories_same_name = await self.by_name(name, user_id)
        except ValueError:
            pass
        else:
            for cat in categories_same_name:
                if cat.parent_id != parent_id:
                    pass
                else:
                    raise ValueError(f"Category with id {name} "
                    f"already exists for parent {parent_id}.")

    async def create(self, category: Category) -> Category:
        category_orm = model_to_orm(
            category,
            CategoryORM,
        )

        try:
            categories_same_name = await self.by_name(
                category.name, category.user_id
            )
        except ValueError:
            pass
        else:
            for cat in categories_same_name:
                if cat.parent_id != category.parent_id:
                    pass
                else:
                    raise ValueError(f"Category with id {category.name} "
                    f"already exists for parent {cat.parent_id}.")

        self._session.add(category_orm)

        await self._session.commit()

        return orm_to_model(
            category_orm,
            Category,
        )

    async def update(self, category: Category) -> Category:
        await self._verify_uq_name_parent(
            category.name, category.parent_id, category.user_id
        )

        query = (
            update(CategoryORM)
            .where(CategoryORM.id == category.id)
            .where(CategoryORM.user_id == category.user_id)
            .values(name=category.name)
        )

        await self._session.execute(query)

        await self._session.commit()

        try:
            updated_cat = await self.by_id(category.id, category.user_id)
        except Exception:
            raise RuntimeError(f"Category with id {category.id} not found.")

        return updated_cat
    
    async def list_childs(
        self,
        category_id: uuid.UUID,
        user_id: uuid.UUID
    ) -> List[Category]:
        query = (
            select(CategoryORM)
            .where(CategoryORM.parent_id == category_id)
            .where(CategoryORM.user_id == user_id)
        )

        result = await self._session.execute(query)

        childs = result.scalars().all()

        return [orm_to_model(
            child, Category,
        ) for child in childs]

    async def delete(
        self, category_id: uuid.UUID, user_id: uuid.UUID) -> None:
        query = (
            delete(CategoryORM)
            .where(CategoryORM.id == category_id)
            .where(CategoryORM.user_id == user_id)
        )

        result = await self._session.execute(query)

        # Verifying if the category was deleted
        if (result.rowcount <= 0): # type: ignore
            raise ValueError(f"Category with id {category_id} not found "
            f"for user {user_id}.")

        await self._session.commit()