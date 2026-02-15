#
#   Imports
#

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime

# Perso

from adapters.shared.dependencies import get_db_session, get_user
from adapters.features.summary.summary_repo import SummaryRepo
from core.shared.models.user import User
from core.shared.enums.trans_type import TransType
from core.features.summary.summary_service import SummaryService

#
#   Routes
#

summary_routes = APIRouter(prefix="/summary")

@summary_routes.get(
    "/balance",
    summary="Get the balance of the user",
)
async def get_summary(
    user: User = Depends(get_user),
    db_session: AsyncSession = Depends(get_db_session),
    year: int = Query(default=datetime.now().year),
    trans_types: list[TransType] = Query(default=[]),
) -> float:
    """
        Gets the balance of the user. For a year and
        depending on the transactions types selected.
    """

    repo = SummaryRepo(session=db_session)

    summary_service = SummaryService(summary_db_port=repo)
    

    balance = await summary_service.get_balance(
        user_id=user.id,
        year=year,
        trans_types=trans_types
    )

    return balance