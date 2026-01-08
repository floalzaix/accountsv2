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
from adapters.features.categories.category_orm import CategoryChildORM, CategoryORM
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

    async def by_id(self, category_id: uuid.UUID) -> Category:
        query = (
            select(CategoryORM)
            .where(CategoryORM.id == category_id)
            .options(selectinload(CategoryORM.parents))
        )

        result = await self._session.execute(query)

        category_orm = result.scalar_one_or_none()

        if category_orm is None:
            raise ValueError(f"Category with id {category_id} not found")

        return orm_to_model(
            category_orm,
            Category,
            exclude=["parents"],
            include={"parent_ids": [
                parent.id
                for parent in category_orm.parents
            ]}
        )

    async def by_name(self, name: str, user_id: uuid.UUID) -> Category:
        query = (
            select(CategoryORM)
            .where(CategoryORM.name == name)
            .where(CategoryORM.user_id == user_id)
            .options(selectinload(CategoryORM.parents))
        )

        result = await self._session.execute(query)

        category_orm = result.scalar_one_or_none()
        
        if category_orm is None:
            raise ValueError(f"Category with name {name} "
            f"not found for user {user_id}.")

        return orm_to_model(
            category_orm,
            Category,
            exclude=["parents"],
            include={"parent_ids": [
                parent.id
                for parent in category_orm.parents
            ]}
        )

    async def by_user_id(self, user_id: uuid.UUID) -> List[Category]:
        query = (
            select(CategoryORM)
            .where(CategoryORM.user_id == user_id)
            .options(selectinload(CategoryORM.parents))
        )

        result = await self._session.execute(query)

        categories = result.scalars().all()

        category_models: List[Category] = [
            orm_to_model(
                cat,
                Category,
                exclude=["parents"],
                include={"parent_ids": [
                    parent.id
                    for parent in cat.parents
                ]}
            )
            for cat in categories
        ]

        return category_models

    async def create(self, category: Category) -> Category:
        # Separating the parent ids as it needs to be added after the 
        # category is created
        parent_ids = category.parent_ids

        category_orm = model_to_orm(
            category,
            CategoryORM,
            exclude=["parent_ids"]
        )

        try:
            await self.by_name(category.name, category.user_id)
        except ValueError:
            pass
        else:
            raise ValueError(f"Category with id {category.name} already exists")

        self._session.add(category_orm)

        #
        #   Adding the parents' relationships
        #
        
        # Getting the parents
        parents: List[CategoryORM] = (
            list((await self._session.execute(
                select(CategoryORM)
                .where(CategoryORM.id.in_(parent_ids))
                .where(CategoryORM.level - category.level == -1)
            )).scalars().all())
        )

        # Checking if all the parents were found and have the correct level
        if len(parents) != len(parent_ids):
            raise RuntimeError("One or more parents is not found or has "
            "an invalid level to be the parent of this category.")

        # Adding the parents' relationships
        for parent_id in parent_ids:
            relationship_orm = CategoryChildORM(
                id=uuid.uuid4(),
                parent_id=parent_id,
                child_id=category.id
            )
            self._session.add(relationship_orm)

        await self._session.commit()

        return orm_to_model(
            category_orm,
            Category,
            exclude=["parents"],
            include={"parent_ids": parent_ids}
        )

