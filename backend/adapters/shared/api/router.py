#
#   Imports
#

from fastapi import APIRouter

# Perso

from adapters.shared.api.routes.auth_routes import auth_routes
from adapters.features.categories.category_routes import category_routes

#
#   Routes
#

routes = APIRouter()

routes.include_router(auth_routes)
routes.include_router(category_routes)
