#
#   Imports
#

import datetime
import uuid

from typing import Optional
from pydantic import BaseModel, Field

# Perso

#
#   DTOs
#

class TransactionBase(BaseModel):
    """
        Base model for a transaction.
    """
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        description="The unique identifier of the transaction"
    )
    user_id: Optional[uuid.UUID] = Field(
        default=None,
        description="The id of the user who made the transaction"
    )
    event_date: datetime.date = Field(
        description="The date of the transaction"
    )
    motive: str = Field(
        description="The motive of the transaction"
    )
    to: str = Field(
        description="The name of the receiver of the transaction"
    )
    bank_date: datetime.date = Field(
        description="The date of the transaction in the bank"
    )
    type: str = Field(
        description="The type of the transaction"
    )
    category1_id: Optional[uuid.UUID] = Field(
        default=None,
        description="The first level category of the transaction"
    )
    category2_id: Optional[uuid.UUID] = Field(
        default=None,
        description="The second level category of the transaction"
    )
    category3_id: Optional[uuid.UUID] = Field(
        default=None,
        description="The third level category of the transaction"
    )
    amount: float = Field(
        description="The amount of the transaction"
    )