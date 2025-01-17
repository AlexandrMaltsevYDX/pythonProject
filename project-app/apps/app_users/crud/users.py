from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from apps.app_users.models import User
from apps.app_users.schemas import UserCreate


async def get_all_users(
    session: AsyncSession,
) -> Sequence[User]:
    stmt = select(User).order_by(User.id)
    result = await session.scalars(stmt)
    return result.all()


async def create_user(
    session: AsyncSession,
    user_create: UserCreate,
) -> UserCreate:
    user = User(**user_create.model_dump())
    session.add(user)
    user = UserCreate(username=user.username, foo=user.foo, bar=user.bar)
    await session.commit()
    return user
