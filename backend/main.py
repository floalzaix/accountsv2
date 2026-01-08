#
#   Imports
#

from fastapi import FastAPI, Request, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

# Perso

from adapters.shared.api.router import routes
from adapters.shared.lifespan import lifespan
from adapters.shared.config.config import get_settings, Env
from core.shared.exceptions.security_error import SecurityError

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
@app.exception_handler(SecurityError)
async def security_error_handler(request: Request, exc: SecurityError):
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail={
            "security_safe_title": "Unauthorized",
            "security_safe_description": "You are not authorized to access this resource.",
            "dev": str(exc)
        }
    )

@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail={
            "user_safe_title": "Erreur inattendue",
            "user_safe_description": "Une erreur inattendue du serveur est survenue.",
            "dev": str(exc)
        }
    )