#
#   Imports
#

import uuid

# Perso

from core.shared.enums.trans_type import TransType
from core.features.summary.summary_port import SummaryDBPort

#
#   Services
#

class SummaryService:
    """
        Service for summary operations.
    """
    def __init__(self, summary_db_port: SummaryDBPort):
        self._summary_db_port = summary_db_port

    async def get_balance(
        self,
        user_id: uuid.UUID,
        year: int,
        trans_types: list[TransType]
    ) -> float:
        return await self._summary_db_port.get_balance(user_id, year, trans_types)