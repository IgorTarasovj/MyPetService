from sqlalchemy import select

from app.db.base import Base
from app.db.session import engine, SessionLocal
from app.db.models.user import User


def init_db() -> None:
    Base.metadata.create_all(bind=engine)

    with SessionLocal() as db:
        user = db.scalar(
            select(User).where(User.username == "admin")
        )

        if user is None:
            user = User(
                username = "admin",
                email="default@example.com"
            )

            db.add(user)
            db.commit()