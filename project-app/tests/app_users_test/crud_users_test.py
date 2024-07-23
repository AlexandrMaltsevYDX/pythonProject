import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from apps.app_users.crud import create_user
from apps.app_users.schemas import UserCreate


@pytest.mark.parametrize(
    ('username', 'foo', 'bar'),
    [('Bob', 8, 1)],
)
async def test_create_user(
    db_session: AsyncSession,
    username: str,
    foo: int,
    bar: int,
) -> None:
    data = UserCreate(
        username=username,
        foo=foo,
        bar=bar,
    )

    user = await create_user(db_session, data)
    assert user.username == 'Bob'
