#
#   Imports
#

import uuid

from dataclasses import dataclass
from typing import List

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
    parent_ids: List[uuid.UUID]