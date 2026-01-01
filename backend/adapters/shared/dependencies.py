#
#   Imports
#

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

# Perso

from adapters.shared.db.bootstrap import get_session

#
#   Dependancies
#

async def get_db_session(
    session: AsyncSession = Depends(get_session)
) -> AsyncSession:
    return session