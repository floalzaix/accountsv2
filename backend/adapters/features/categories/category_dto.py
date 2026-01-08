#
#   Imports
#

import uuid

from typing import List
from pydantic import BaseModel, Field

# Perso

#
#   DTOs
#

class CategoryBase(BaseModel):
    """
        Base model for a category.
    """
    name: str = Field(
        min_length=1,
        max_length=255,
        description="The category's name"
    )
    user_id: uuid.UUID = Field(
        description="The user's unique identifier"
    )

class CategoryRead(CategoryBase):
    """
        Model for reading a category.
    """
    id: uuid.UUID = Field(
        ...,
        description="The category's unique identifier"
    )
    level: int = Field(
        ...,
        ge=0,
        le=3,
        description="The category's level"
    )
    parent_ids: List[uuid.UUID] = Field(
        ...,
        description="The parent categories' unique identifiers"
    )

class CategoryCreate(CategoryBase):
    """
        Model for creating a category.
    """
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        description="The category's unique identifier"
    )
    level: int = Field(
        ...,
        ge=0,
        le=3,
        description="The category's level"
    )
    parent_ids: List[uuid.UUID] = Field(
        ...,
        description="The parent categories' unique identifiers"
    )

class CategoryUpdate(CategoryBase):
    """
        Model for updating a category.
    """
    id: uuid.UUID = Field(
        description="The category's unique identifier"
    )