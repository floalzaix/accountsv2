#
#   Imports
#

import uuid

from abc import ABC, abstractmethod

# Perso

from core.features.categories.category import Category

#
#   Ports
#

class CategoryDBPort(ABC):

    @abstractmethod
    async def by_id(self, category_id: uuid.UUID) -> Category:
        pass
