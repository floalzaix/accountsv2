#
#   Imports
#

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

# Perso

from adapters.shared.dependencies import get_db_session, get_user
from core.shared.models.user import User
from adapters.features.details.details_repo import DetailsRepo, DetailsTabType
from core.features.details.details_service import DetailsService
from adapters.features.details.details_dto import DetailsCategoryRowDTO


#
#   Routes
#

details_routes = APIRouter(prefix="/details")


@details_routes.get(
    "/",
    response_model=DetailsCategoryRowDTO,
)
async def get_detailed_tab(
    user: User = Depends(get_user),
    db_session: AsyncSession = Depends(get_db_session),
):
    repo = DetailsRepo(session=db_session)
    service = DetailsService(repo)

    return await service.get_detailed_tab(
        year=2024,
        trans_type="debit",
        user_id=user.id,
        tab_type=DetailsTabType.REVENUES
    )