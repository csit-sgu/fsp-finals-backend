from datetime import date, datetime
from typing import ClassVar
from uuid import UUID

from shared.db import Entity


class User(Entity):
    id: UUID
    username: str
    password: bytes
    is_admin: bool
    birth_date: date
    name: str
    surname: str
    weekly_goal: float

    _table_name: ClassVar[str] = "users"
    _pk: ClassVar[str] = "id"


class Quiz(Entity):
    quiz_id: int
    title: str
    author_id: UUID
    description: str
    category: str
    entry_id: UUID

    _table_name: ClassVar[str] = "quizzes"
    _pk = "quiz_id"


class Block(Entity):
    block_id: UUID
    block_type: str
    payload: str  # json?

    _table_name: ClassVar[str] = "blocks"
    _pk = "block_id"


# class QuizBlock(Entity):
#     task_id: UUID
#     block_id: UUID

#     _table_name: ClassVar[str] = "quiz_block"


class Attempt(Entity):
    attempt_id: int
    quiz_id: int
    user_id: UUID
    quiz_score: float
    time_passed: int
    start_timestamp: datetime

    _table_name: ClassVar[str] = "attempts"
    _pk = "attempt_id"


class QuizComplexity(Entity):
    quiz_id: UUID
    age_category: str
    complexity: str

    _table_name: ClassVar[str] = "quiz_complexities"


class RunningContainer(Entity):
    container_id: str
    user_id: UUID
    block_id: UUID
    start_timestamp: datetime
    host_ip: str
    host_port: str

    _table_name: ClassVar[str] = "running_containers"