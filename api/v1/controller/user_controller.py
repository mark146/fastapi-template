from fastapi import APIRouter

from api.v1.dto.response.ApiResponse import ApiResponse
from api.v1.service import user_service

router = APIRouter()


@router.get("")
async def get_users():
    return ApiResponse.ok(await user_service.get_users())
