from fastapi import APIRouter

from app.schemas.technical.technical import StatusResponseSchema

router = APIRouter(prefix="", tags=["Status"])

@router.get("/status",
            response_model=StatusResponseSchema)
def get_status() -> StatusResponseSchema:
    """
    Метод проверки доступности сервиса
    :return: StatusResponseSchema
    """
    return StatusResponseSchema()