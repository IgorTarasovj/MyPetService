import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.db.dependencies import get_db, get_user_repository
from app.db.models.user import User
from app.schemas.user.user import UserRequestSchema, UserResponseSchema
from app.db.repositories.user_repository import UserRepository

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

@router.post("/user", response_model=UserResponseSchema)
def create_user(request: UserRequestSchema,
                user_repository: UserRepository = Depends(get_user_repository)) -> UserResponseSchema:
    try:
        user = user_repository.create_user(
            username=request.username,
            email=request.email
        )

        return UserResponseSchema(
            id=user.id,
            username=user.username,
            email=user.email,
        )
    except IntegrityError:
        raise HTTPException(status_code=409, detail="User already exists")