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
    email: str