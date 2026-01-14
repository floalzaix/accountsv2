#
#   Imports
#

from __future__ import annotations

import uuid

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import CheckConstraint, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID

# Perso

from adapters.shared.db.base import Base
from adapters.shared.db.orms.user_orm import UserORM

#
#   ORMs
#

class CategoryORM(Base):
    """
        Represents a category in the database.
    """

    __tablename__ = "categories"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        doc="The category's unique identifier",
    )
    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        doc="The category's name",
    )
    level: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        doc="The category's level",
    )
    parent_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("categories.id", ondelete="CASCADE"),
        nullable=True,
        doc="The parent category's unique identifier",
    )
    

    #
    #   Foreign Keys
    #
    
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        doc="The user's unique identifier",
    )

    #
    #   Relationships
    #
    
    user: Mapped[UserORM] = relationship(
        "UserORM",
        back_populates="categories",
        doc="The user that owns the category",
    )

    #
    #   Constraints
    #
    
    __table_args__ = (
        CheckConstraint("level >= 0", name="ck_level_ge_0"),
        UniqueConstraint("parent_id", "name", name="uq_parent_id_name"),
    )
    