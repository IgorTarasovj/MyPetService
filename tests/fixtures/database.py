import pytest
from sqlalchemy.orm import Session

from src.db.db_client import DatabaseClient
from src.db.repositories.user_repository import UserRepository

database_url = "sqlite:///./database.db"

@pytest.fixture
def db_client() -> Session:
    client = DatabaseClient(database_url)

    yield client

    client.close()

@pytest.fixture
def users_repository(
    db_client: DatabaseClient,
) -> UserRepository:

    return UserRepository(db_client)