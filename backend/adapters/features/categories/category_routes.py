#
#   Imports
#

from fastapi import APIRouter, Depends, status, HTTPException

# Perso

from adapters.shared.dependencies import get_db_session

#
#   Routes
#

category_routes = APIRouter(prefix="/categories")