#
#   Imports
#

import uuid

# Perso

from core.features.details.details_port import DetailsDBPort
from adapters.features.details.details_repo import DetailsTabType
from core.features.details.details import DetailsTab

#
#   Details Service
#

class DetailsService:
    def __init__(self, details_repo: DetailsDBPort):
        self.details_repo = details_repo

    async def get_detailed_tab(
        self,
        year: int,
        trans_type: str,
        user_id: uuid.UUID,
        tab_type: DetailsTabType
    ) -> DetailsTab:
        return await self.details_repo.get_detailed_tab(
            year=year,
            trans_type=trans_type,
            user_id=user_id,
            tab_type=tab_type
        )