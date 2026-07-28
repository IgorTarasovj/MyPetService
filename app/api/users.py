import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.db.models.user import User
from app.schemas.user.user import UserRequestSchema, UserResponseSchema

router = APIRouter(prefix="/users",
    tags=["Users"])

@router.get("/user",
            response_model=UserResponseSchema)
def get_user(user_id: uuid.UUID,
             db: Session = Depends(get_db)) -> UserResponseSchema:
    """
    Метод проверки доступности сервиса
    :return: StatusResponseSchema
    """
    user = db.scalar(
        select(User).where(User.id == user_id)
    )

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user