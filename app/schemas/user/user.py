import uuid

from pydantic import BaseModel, Field, ConfigDict, EmailStr


class UserRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание пользователя
    """
    username: str
    email: EmailStr

class UserResponseSchema(BaseModel):
    """
    Описание структуры овтета на создание пользователя
    """
    id: uuid.UUID
    username: str
    email: EmailStr

class UserUpdateRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление пользователя
    """
    id: uuid.UUID
    username: str | None = None
    email: EmailStr | None = None

class UserUpdateResponseSchema(BaseModel):
    """
    Описание структуры ответа на обновление пользователя
    """
    id: uuid.UUID
    username: str
    email: EmailStr

class UserDeleteRequestSchema(BaseModel):
    """
    Описание структуры запроса на удаление пользователя
    """
    id: uuid.UUID

class UserDeleteResponseSchema(BaseModel):
    """
     Описание структуры ответа на обновление пользователя
    """
    status: str = Field(default= "OK")
    username: str
    email: EmailStr