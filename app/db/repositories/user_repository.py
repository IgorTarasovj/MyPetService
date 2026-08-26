import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models.user import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, username: str, email: str)->User:
        user = User(id= uuid.uuid4(), username=username, email=email)

        self.db.add(user)
        self.db.commit()

        return user

    def update_user(self, user_id, username: str, email: str)->User:
        user = self.db.scalar(
            select(User).where(User.id == user_id)
        )

        if user is None:
            return None

        user.username = username
        user.email = email

        self.db.commit()

        return user