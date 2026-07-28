import uuid

from pydantic import BaseModel, Field


class UserRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание пользователя
    """
    username: str
    id: str

class UserResponseSchema(BaseModel):
    """
    Описание структуры овтета на создание пользователя
    """
    username: str
    email: str