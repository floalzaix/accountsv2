#
#   Imports
#

import uuid

from abc import ABC, abstractmethod

# Perso

from core.shared.enums.trans_type import TransType

#
#   Ports
#

class SummaryDBPort(ABC):
    
    @abstractmethod
    async def get_balance(
        self,
        user_id: uuid.UUID,
        year: int,
        trans_types: list[TransType]
    ) -> float:
        """
            Gets the balance of the user. For a year and
            depending on the transactions types selected.

            It basically filters the transactions and makes 
            a sum of the amounts.
        """
        pass