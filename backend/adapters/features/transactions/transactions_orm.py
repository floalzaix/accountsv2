#
#   Imports
#

import uuid
import datetime

from sqlalchemy import ForeignKey

from adapters.shared.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import DateTime, String, Float

# Perso

from adapters.shared.db.orms.user_orm import UserORM

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
    event_date: Mapped[datetime.datetime] = mapped_column(
        DateTime,
        nullable=False,
        doc="The date of the transaction",
    )
    motive: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        doc="The amount of money in the transaction",
    )
    to: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        nullable=False,
        doc="The user's id who received the money",
    )
    bank_date: Mapped[datetime.datetime] = mapped_column(
        DateTime,
        nullable=False,
        doc="The date of the transaction in the bank",
    )
    type: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        doc="The type of the transaction",
    )
    status: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        doc="The status of the transaction",
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
    
    #
    #   Relationships
    #

    user: Mapped[UserORM] = relationship(
        "UserORM",
        back_populates="transactions",
        doc="The user who made the transaction",
    )
    