from apps.app_users.crud.users import create_user
from apps.app_users.schemas import UserCreate
from tests.conftest import test_db_helper


async def test_create_user() -> None:
    session = test_db_helper.session_getter()
    new_fix_user = UserCreate(username='Test', foo=1, bar=2)
    new_user = await create_user(session, new_fix_user)
    assert new_user.username == 'Test'
