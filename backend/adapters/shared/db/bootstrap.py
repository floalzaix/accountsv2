#
#   Imports
#

from typing import AsyncGenerator, Optional
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
    AsyncEngine,
)
from sqlalchemy import text

# Personal

from adapters.shared.config.config import get_settings, Env

#
#   Bootstrap
#

settings = get_settings()

_session_maker: Optional[async_sessionmaker[AsyncSession]] = None

async def bootstrap_db() -> None:
    """
        Bootstrap the database by setting up the engine and the session maker.
    """
    global _session_maker

    if _session_maker is not None:
        return

    URL = (
        f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@"
        f"{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
    )

    # Creating the engine
    engine: AsyncEngine = create_async_engine(
        URL,
        echo=settings.APP_ENV == Env.DEVELOPMENT,
    )

    # Creating the session maker
    _session_maker = async_sessionmaker[AsyncSession](
        engine,
        expire_on_commit=False,
    )

    # Trying peremissions and at least one table exists
    try:
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
    except Exception as e:
        raise RuntimeError(
            "Error verifying permissions or table existence. "
            "Please check your database configuration. \n"
            f"Error: {e}"
        ) from e

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """
        Get a session from the session maker.
    """
    if _session_maker is None:
        raise RuntimeError(
            "Trying to access database before it has been initialized."
        )

    async with _session_maker() as session:
        try:
            yield session

        except Exception as e:
            await session.rollback()
            raise e
