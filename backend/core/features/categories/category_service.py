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

    