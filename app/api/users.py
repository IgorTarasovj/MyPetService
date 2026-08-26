import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.db.dependencies import get_db, get_user_repository
from app.db.models.user import User
from app.schemas.user.user import UserRequestSchema, UserResponseSchema, UserUpdateRequestSchema, \
    UserUpdateResponseSchema
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
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

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
            email=user.email
        )
    except IntegrityError:
        raise HTTPException(status_code=409, detail="User already exists")

@router.put("/user", response_model=UserUpdateResponseSchema)
def update_user(request: UserUpdateRequestSchema,
                user_repository: UserRepository = Depends(get_user_repository)) -> UserUpdateResponseSchema:

    user = user_repository.update_user(
        user_id=request.id,
        username=request.username,
        email=request.email,
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return UserUpdateResponseSchema(
        id=user.id,
        username=user.username,
        email=user.email
    )

@router.patch("/user", response_model=UserUpdateResponseSchema)
def partial_update_user(request: UserUpdateRequestSchema,
                        user_repository: UserRepository = Depends(get_user_repository)) -> UserUpdateResponseSchema:

    user = user_repository.update_user(
        user_id=request.id,
        username=request.username,
        email=request.email,
    )

    if user.username is None and user.email is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="At least one field must be provided",
        )


    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )


    return UserUpdateResponseSchema(
        id=user.id,
        username=user.username,
        email=user.email
    )