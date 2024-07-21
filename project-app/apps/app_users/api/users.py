from typing import Annotated
from typing import Sequence

from fastapi import (
    APIRouter,
    Depends,
)
from sqlalchemy.ext.asyncio import AsyncSession

from apps.app_users.crud import users as users_crud
from apps.app_users.models import User
from apps.app_users.schemas import UserRead, UserCreate
from core.db.helper import db_helper
from core.settings.app_config import settings

router = APIRouter(
    prefix=settings.api.v1.users,
    tags=['Users'],
)


@router.get('', response_model=list[UserRead])
async def get_users(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
) -> Sequence[User]:
    users = await users_crud.get_all_users(session=session)
    return users  # noqa: RET504


@router.post('', response_model=UserRead)
async def create_user(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    user_create: UserCreate,
) -> User:
    user = await users_crud.create_user(
        session=session,
        user_create=user_create,
    )
    return user  # noqa: RET504
