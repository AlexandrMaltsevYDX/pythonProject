# !todo fixme bad naming
import pytest
from fastapi.testclient import TestClient
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

from core.db import Base
from core.db.helper import DatabaseHelper, db_helper
from core.settings.app_config import ApiPrefix
from core.settings.app_config import DatabaseConfig
from core.settings.app_config import RunConfig
from main import main_app


class TestSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(
            '.env.test-this-project',
        ),  # u can use inheritance envs files
        case_sensitive=False,
        env_nested_delimiter='__',
        env_prefix='APP_CONFIG__',
    )
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig


settings = TestSettings()

test_db_helper = DatabaseHelper(
    url=str(settings.db.url),
    echo=settings.db.echo,
    echo_pool=settings.db.echo_pool,
    pool_size=settings.db.pool_size,
    max_overflow=settings.db.max_overflow,
)

main_app.dependency_overrides[db_helper.session_getter] = (
    test_db_helper.session_getter
)

client = TestClient(main_app)


@pytest.fixture(autouse=True, scope='session')
async def _prepare_database() -> None:
    async with test_db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with test_db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
