#
#   Imports
#

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
        "User",
        back_populates="categories",
        cascade="all, delete-orphan",
        doc="The user that owns the category",
    )

    #
    #   Constraints
    #
    
    __table_args__ = (
        UniqueConstraint("name", "user_id", name="uq_name_user_id"),
        CheckConstraint("level >= 0", name="ck_level_ge_0"),
    )

class CategoryChildORM(Base):
    """
        Represents a category child in the database.

        To persist the relationships between categories and their children.
    """

    __tablename__ = "categories_childs"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        doc="The relationship's unique identifier",
    )
    parent_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("categories.id", ondelete="CASCADE"),
        nullable=False,
        doc="The parent category's unique identifier",
    )
    child_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("categories.id", ondelete="CASCADE"),
        nullable=False,
        doc="The child category's unique identifier",
    )