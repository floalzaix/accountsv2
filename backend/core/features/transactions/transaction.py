#
#   Imports
#

import uuid
import datetime

from dataclasses import dataclass
from typing import Optional

# Perso

#
#   Models
#

@dataclass
class Transaction:
    """
        Represents a transaction.
    """
    id: uuid.UUID
    event_date: datetime.datetime
    motive: str
    to: str
    bank_date: datetime.datetime
    type: str
    category1_id: Optional[uuid.UUID]
    category2_id: Optional[uuid.UUID]
    category3_id: Optional[uuid.UUID]
    amount: float
    user_id: uuid.UUID