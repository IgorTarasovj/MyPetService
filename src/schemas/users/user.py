import uuid

from pydantic import BaseModel, Field


class User(BaseModel):
    """
    Описание структуры пользователя
    """
    id: uuid.UUID
    username: str
    email: str

class UserDBSchema(BaseModel):
    """
    Описание структуры таблицы users в базе данных
    """
    id: uuid.UUID
    username: str
    email: str

class GerUserResponseSchema(BaseModel):
    """
    Описание структуры ответа на GET запрос /user
    """
    username: str
    email: str

