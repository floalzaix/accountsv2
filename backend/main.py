#
#   Imports
#

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Perso

from adapters.api.router import routes

#
#   App
#

app = FastAPI() 

# Adding the CROSS security

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Adding the routes

app.include_router(routes, prefix="/api")

# Handling global exceptions