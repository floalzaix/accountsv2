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

class UserLogin(BaseModel):
    """
        Model for logging in a user.
    """
    email: str = Field(
        min_length=1,
        max_length=255,
        description="The user's email address"
    )
    password: str = Field(
        min_length=1,
        max_length=255,
        description="The user's password"
    )

class UserBearer(BaseModel):
    """
        Model for a user bearer.
    """
    access_token: str = Field(
        description="The user's access token"
    )
    user: UserRead = Field(
        description="The user"
    )
    token_type: str = Field(
        description="The token type"
    )