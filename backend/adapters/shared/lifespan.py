#
#   Imports
#

from contextlib import asynccontextmanager
from fastapi import FastAPI
from typing import AsyncGenerator

# Perso

from adapters.shared.db.bootstrap import bootstrap_db

#
#   Lifespan
#

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """
        Lifespan for the application.
    """
    await bootstrap_db()

    yield
