#
#   Imports
#

from typing import List
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

# Perso

from adapters.shared.dependencies import get_db_session, get_user
from core.shared.models.user import User
from adapters.features.details.details_repo import DetailsRepo, DetailsTabType
from core.features.details.details_service import DetailsService
from adapters.features.details.details_dto import DetailsTabDTO


#
#   Routes
#

details_routes = APIRouter(prefix="/details")


@details_routes.get(
    "/",
    response_model=DetailsTabDTO,
    summary="Get a detailed tab of the transactions",
)
async def get_detailed_tab(
    year: int = Query(..., description="The year of the transactions"),
    trans_types: List[str] = Query(..., description="The types of the transactions"),
    tab_type: DetailsTabType = Query(..., description="The type of the tab"),
    user: User = Depends(get_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    repo = DetailsRepo(session=db_session)
    service = DetailsService(repo)

    details_tab = await service.get_detailed_tab(
        year=year,
        trans_types=trans_types,
        user_id=user.id,
        tab_type=tab_type
    )

    return details_tab