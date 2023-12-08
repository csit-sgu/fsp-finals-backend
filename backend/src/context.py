from os import getenv

from databases import Database
from dotenv import load_dotenv

from shared.db import PgRepository, create_db_string
from shared.resources import SharedResources
from shared.utils import SHARED_CONFIG_PATH
from entities import (
    User,
    Task,
    Block,
    Attempt,
    TaskComplexity,
    RunningContainer,
)


class Context:
    def __init__(self):
        self.shared_settings = SharedResources(
            f"{SHARED_CONFIG_PATH}/settings.json"
        )
        self.pg = Database(create_db_string(self.shared_settings.pg_creds))
        self.user_repo = PgRepository(self.pg, User)
        self.task_repo = PgRepository(self.pg, Task)
        self.block_repo = PgRepository(self.pg, Block)
        self.attempt_repo = PgRepository(self.pg, Attempt)
        self.complexity_repo = PgRepository(self.pg, TaskComplexity)
        self.container_repo = PgRepository(self.pg, RunningContainer)

        self.access_token_expire_minutes = int(
            getenv("ACCESS_TOKEN_EXPIRE_MINUTES") or 5
        )
        self.refresh_token_expire_minutes = int(
            getenv("REFRESH_TOKEN_EXPIRE_MINUTES") or 60
        )
        self.jwt_secret_key = getenv("JWT_SECRET_KEY") or "secret"
        self.jwt_refresh_secret_key = getenv("JWT_SECRET_KEY") or "secret"
        self.hash_algorithm = getenv("ALGORITHM") or "HS256"

    async def init_db(self) -> None:
        await self.pg.connect()

    async def dispose_db(self) -> None:
        await self.pg.disconnect()


load_dotenv()
ctx = Context()
