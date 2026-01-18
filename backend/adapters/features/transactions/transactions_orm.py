#
#   Imports
#

import uuid
import datetime

from sqlalchemy import ForeignKey, UniqueConstraint

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

    #
    #   Constraints
    #
    
    __table_args__ = (
        UniqueConstraint("event_date", "motive", "to", "bank_date", "type", "amount", "user_id", name="uix_event_date_motive_to_bank_date_type_amount_user_id"),
    )
    
class TransactionCategoriesORM(Base):
    __tablename__ = "transactions_categories"
    
    """
        Links the three levels of the categories linked to a transaction.
    """

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        doc="The transaction category's unique identifier",
    )

    #
    #   Foreign Keys
    #

    transaction_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("transactions.id", ondelete="CASCADE"),
        nullable=False,
        unique=True,
        doc="The transaction's id",
    )
    category1_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("categories.id", ondelete="CASCADE"),
        nullable=False,
        doc="The first level category's id",
    )
    category2_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("categories.id", ondelete="CASCADE"),
        doc="The second level category's id",
    )
    category3_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("categories.id", ondelete="CASCADE"),
        doc="The third level category's id",
    )