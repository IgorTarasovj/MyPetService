from collections.abc import Generator

from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.repositories.user_repository import UserRepository
from app.db.session import SessionLocal


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

def get_user_repository(
    db: Session = Depends(get_db),
) -> UserRepository:
    return UserRepository(db)