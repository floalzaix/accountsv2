#
#   Imports
#

import uuid
from pydantic import BaseModel
from pydantic import Field

# Perso

from core.shared.enums.user_status import UserStatus

#
#   DTOs
#

class UserBase(BaseModel):
    """
        Base model for a user.
    """
    email: str = Field(
        min_length=1,
        max_length=255,
        description="The user's email address"
    )
    pseudo: str = Field(
        min_length=1,
        max_length=255,
        description="The user's nickname"
    )

class UserUpdate(UserBase):
    """
        Model for updating a user.
    """
    id: uuid.UUID = Field(
        description="The user's unique identifier"
    )

class UserRead(UserUpdate):
    """
        Model for reading a user.
    """
    status: UserStatus = Field(
        description="The user's status"
    )

class UserCreate(UserBase):
    """
        Model for creating a user.
    """
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        description="The user's unique identifier"
    )
    password: str