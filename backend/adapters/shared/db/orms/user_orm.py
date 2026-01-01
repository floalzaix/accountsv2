#
#   Imports
#

import uuid
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import Enum

# Perso

from adapters.shared.db.base import Base
from core.shared.enums.user_status import UserStatus

#
#   ORMs
#

class User(Base):
    """
        Represents a user in the database.
    """

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        description="The user's unique identifier"
    )
    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        description="The user's email address"
    )
    hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        description="The user's password hash"
    )
    pseudo: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        description="The user's nickname"
    )
    status: Mapped[UserStatus] = mapped_column(
        Enum(UserStatus),
        nullable=False,
        description="The user's status"
    )