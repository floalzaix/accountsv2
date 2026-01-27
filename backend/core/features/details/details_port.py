#
#   Imports
#

import uuid
from abc import ABC, abstractmethod

# Perso

from adapters.features.details.details_repo import DetailsTabType

#
#   
#

class DetailsDBPort(ABC):

    @abstractmethod
    async def get_detailed_tab(
        self,
        year: int,
        trans_type: str,
        user_id: uuid.UUID,
        tab_type: DetailsTabType
    ) -> None:
        pass
