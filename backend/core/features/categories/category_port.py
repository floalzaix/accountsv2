#
#   Imports
#

import uuid

from typing import List
from abc import ABC, abstractmethod

# Perso

from core.features.categories.category import Category

#
#   Ports
#

class CategoryDBPort(ABC):

    @abstractmethod
    async def by_id(self, category_id: uuid.UUID) -> Category:
        """
            Gets a Category by id.

            Params:
                - category_id: The id of the category to get.

            Returns:
                - The category.

            Raises:
                - ValueError: If the category is not found.
        """
        pass

    @abstractmethod
    async def by_name(self, name: str, user_id: uuid.UUID) -> Category:
        """
            Gets a Category by name.

            Params:
                - name: The name of the category to get.
                - user_id: The user's unique identifier.

            Returns:
                - The category.

            Raises:
                - ValueError: If the category is not found.
        """
        pass

    @abstractmethod
    async def by_user_id(self, user_id: uuid.UUID) -> List[Category]:
        """
            Lists all categories for a given user in the db.

            Params:
                - user_id: The user's unique identifier.

            Returns:
                - A list of categories.
        """
        pass

    @abstractmethod
    async def create(self, category: Category) -> Category:
        """
            Creates a category.

            Params:
                - category: The category to create.

            Returns:
                - The created category.
        """
        pass