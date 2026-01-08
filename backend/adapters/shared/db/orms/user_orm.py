#
#   Imports
#

from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import Enum

# Perso

from adapters.shared.db.base import Base
from core.shared.enums.user_status import UserStatus

if TYPE_CHECKING:
    from adapters.features.categories.category_orm import CategoryORM

#
#   ORMs
#

class UserORM(Base):
    """
        Represents a user in the database.
    """

    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        doc="The user's unique identifier",
    )
    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        doc="The user's email address",
    )
    hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        doc="The user's password hash",
    )
    pseudo: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        doc="The user's nickname",
    )
    status: Mapped[UserStatus] = mapped_column(
        Enum(UserStatus),
        nullable=False,
        doc="The user's status",
    )

    #
    #   Relationships
    #
    
    categories: Mapped[list[CategoryORM]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
        doc="The categories owned by the user",
    )