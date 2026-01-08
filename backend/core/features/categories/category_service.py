#
#   Imports
#


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

    