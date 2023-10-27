from fastapi import APIRouter

from api.v1.controller import user_controller

router_v1 = APIRouter()

router_v1.include_router(user_controller.router, prefix="/users", tags=["users"])
