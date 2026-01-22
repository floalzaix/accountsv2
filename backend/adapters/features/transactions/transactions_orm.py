#
#   Imports
#

from __future__ import annotations

import uuid
import datetime

from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, UniqueConstraint
from adapters.shared.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import DateTime, String, Float

# Perso

from adapters.shared.db.orms.user_orm import UserORM

if TYPE_CHECKING:
    from adapters.features.categories.category_orm import CategoryORM

#
#   ORMs
#

class TransactionORM(Base):
    __tablename__ = "transactions"
    
    """
        Represents a transaction in the database.
    """

    __tablename__ = "transactions"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        doc="The transaction's unique identifier",
    )
    event_date: Mapped[datetime.date] = mapped_column(
        DateTime,
        nullable=False,
        doc="The date of the transaction",
    )
    motive: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        doc="The amount of money in the transaction",
    )
    to: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        doc="The name of the receiver of the transaction",
    )
    bank_date: Mapped[datetime.date] = mapped_column(
        DateTime,
        nullable=False,
        doc="The date of the transaction in the bank",
    )
    type: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        doc="The type of the transaction",
    )
    amount: Mapped[float] = mapped_column(
        Float,
        nullable=False,
        doc="The amount of money in the transaction",
    )

    #
    #   Foreign Keys
    #

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        doc="The user's id who made the transaction",
    )
    category1_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("categories.id", ondelete="SET NULL"),
        doc="The first level category's id",
    )
    category2_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("categories.id", ondelete="SET NULL"),
        doc="The second level category's id",
    )
    category3_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("categories.id", ondelete="SET NULL"),
        doc="The third level category's id",
    )
    
    #
    #   Relationships
    #

    user: Mapped[UserORM] = relationship(
        "UserORM",
        back_populates="transactions",
        doc="The user who made the transaction",
    )

    category1: Mapped[CategoryORM] = relationship(
        "CategoryORM",
        foreign_keys=[category1_id],
        doc="The first level category of the transaction",
    )
    category2: Mapped[CategoryORM] = relationship(
        "CategoryORM",
        foreign_keys=[category2_id],
        doc="The second level category of the transaction",
    )
    category3: Mapped[CategoryORM] = relationship(
        "CategoryORM",
        foreign_keys=[category3_id],
        doc="The third level category of the transaction",
    )

    #
    #   Constraints
    #
    
    __table_args__ = (
        UniqueConstraint("event_date", "motive", "to", "bank_date", "type", "amount", "user_id", "category1_id", "category2_id", "category3_id", name="uq_transaction_unique"),
    )