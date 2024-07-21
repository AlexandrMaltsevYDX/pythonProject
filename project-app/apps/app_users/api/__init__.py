from fastapi import APIRouter

from core.settings.app_config import settings
from .users import router as users_router

router_v1 = APIRouter(
    prefix=settings.api.v1.prefix,
)

router_v1.include_router(
    users_router,
)
