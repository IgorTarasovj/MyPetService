from pydantic import BaseModel, Field


class GetResponseStatusSchema(BaseModel):
    """
    Описание структуры ответа статуса сервиса
    """
    status: str = Field(default="OK")