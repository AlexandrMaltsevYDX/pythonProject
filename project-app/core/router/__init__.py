from fastapi import APIRouter

from apps.app_users.api import router_v1
from core.settings import settings

main_router = APIRouter(
    prefix=settings.api.prefix,
)
main_router.include_router(
    router_v1,
)
