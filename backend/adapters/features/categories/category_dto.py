#
#   Imports
#

import uuid

from typing import Optional
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
        ...,
        min_length=1,
        max_length=255,
        description="The category's name"
    )
    user_id: Optional[uuid.UUID] = Field(
        default=None,
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
        le=2,
        description="The category's level"
    )
    parent_id: Optional[uuid.UUID] = Field(
        default=None,
        description="The parent category's unique identifier"
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
        le=2,
        description="The category's level"
    )
    parent_id: Optional[uuid.UUID] = Field(
        default=None,
        description="The parent category's unique identifier"
    )

class CategoryUpdate(CategoryBase):
    """
        Model for updating a category.
    """
    id: Optional[uuid.UUID] = Field(
        default=None,
        description="The category's unique identifier"
    )