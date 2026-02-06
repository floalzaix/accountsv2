#
#   Imports
#

from fastapi import APIRouter

# Perso

from adapters.shared.api.routes.auth_routes import auth_routes
from adapters.features.categories.category_routes import category_routes
from adapters.features.transactions.transactions_routes import transactions_routes
from adapters.features.details.details_routes import details_routes
from adapters.features.summary.summary_routes import summary_routes

#
#   Routes
#

routes = APIRouter()

routes.include_router(auth_routes)
routes.include_router(category_routes)
routes.include_router(transactions_routes)
routes.include_router(details_routes)
routes.include_router(summary_routes)