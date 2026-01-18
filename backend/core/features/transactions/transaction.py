#
#   Imports
#

import uuid
import datetime

# Perso


#
#   Models
#

class Transaction:
    """
        Represents a transaction.
    """
    id: uuid.UUID
    event_date: datetime.datetime
    motive: str
    to: uuid.UUID
    bank_date: datetime.datetime
    type: str
    amount: float