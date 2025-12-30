#
#   Imports
#

from fastapi import APIRouter

# Perso

from adapters.shared.api.routes.auth_routes import auth_routes

#
#   Routes
#

routes = APIRouter()

routes.include_router(auth_routes)
