import uuid

from pydantic import BaseModel, Field


class User(BaseModel):
    id: uuid.UUID
    username: str
    email: str

class UserDBSchema(BaseModel):
    id: uuid.UUID
    username: str
    email: str

class GerUserResponseSchema(BaseModel):
    username: str
    email: str

