from fastapi import Depends
from fastapi.routing import APIRouter

from api.deps import get_current_active_user
from core.ds import UserModel

profile_route = APIRouter()

@profile_route.get('/users/me', response_model=UserModel)
async def read_user(current_user: UserModel = Depends(get_current_active_user)):
    return current_user

