#
#   Imports
#

import uuid

from dataclasses import dataclass

# Perso

#
#   Models
#

@dataclass
class Category:
    """
        Represents a category.
    """

    id: uuid.UUID
    name: str
    level: int
    user_id: uuid.UUID