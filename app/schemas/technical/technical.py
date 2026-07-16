from pydantic import BaseModel, Field


class StatusResponseSchema(BaseModel):
    """
    Описание структуры ответа статуса сервиса
    """
    status: str = Field(default ="OK")
