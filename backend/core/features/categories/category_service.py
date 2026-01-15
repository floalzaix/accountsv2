#
#   Imports
#

import uuid

from typing import List

# Perso

from core.features.categories.category import Category
from core.features.categories.category_port import CategoryDBPort

#
#   Service
#

class CategoryService:
    """
        Service for category operations.
    """

    def __init__(self, category_db_port: CategoryDBPort):
        self._category_db_port = category_db_port

    async def list_categories(self, user_id: uuid.UUID) -> List[Category]:
        """
            Lists all categories for a given user.

            Params:
                - user_id: The user's unique identifier.

            Returns:
                - A list of categories.
        """
        return await self._category_db_port.by_user_id(user_id)

    async def create_category(self, category: Category) -> Category:
        """
            Creates a category.

            Params:
                - category: The category to create.

            Returns:
                - The created category.

            Raises:
                - ValueError: If the category name is already in use.
                - RuntimeError: If one or more parents is not found
                or has an invalid level to be the parent of this category.
        """
        category = await self._category_db_port.create(category)

        return category

    async def update_category(
        self,
        category_id: uuid.UUID,
        user_id: uuid.UUID,
        name: str
    ) -> Category:
        """
            Updates a category.

            Params:
                - category_id: The category's unique identifier.
                - user_id: The user's unique identifier.
                - name: The new name of the category.

            Returns:
                - The updated category.

            Raises:
                - RuntimeError: If the category is not found.
                - ValueError: If the category name is already in use.
        """
        try:
            category = await self._category_db_port.by_id(category_id, user_id)
        except Exception:
            raise RuntimeError(f"Category with id {category_id} not found.")

        category.name = name

        await self._category_db_port.update(category)

        return category

    async def delete_category(
        self,
        category_id: uuid.UUID,
        user_id: uuid.UUID
    ) -> None:
        """
            Deletes a category.

            Recursively deletes the category and all its childs.
        """

        childs = await self._category_db_port.list_childs(
            category_id, user_id
        )

        for child in childs:
            await self.delete_category(child.id, user_id)

        await self._category_db_port.delete(category_id, user_id)