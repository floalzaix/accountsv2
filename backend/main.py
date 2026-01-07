#
#   Imports
#

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Perso

from adapters.shared.api.router import routes
from adapters.shared.lifespan import lifespan

from adapters.shared.config.config import get_settings, Env

settings = get_settings()

app = FastAPI(lifespan=lifespan)

# Adding the CROSS security

app.add_middleware(
    CORSMiddleware,
    allow_origins= ["*"]
    if settings.APP_ENV == Env.DEVELOPMENT
    else settings.CORS_ALLOW_ORIGINS_PROD,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Adding the routes

app.include_router(routes, prefix="/api")

# Handling global exceptions