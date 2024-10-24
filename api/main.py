from fastapi.routing import APIRouter

from api.routes.profile import profile_route
from api.routes.token import token_router

api_router = APIRouter()

api_router.include_router(token_router, tags=["Token API Endpoint"])
api_router.include_router(profile_route, tags=["Profile API Endpoint"])
