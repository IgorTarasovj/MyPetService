from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.schemas.technical.technical import StatusResponseSchema

router = APIRouter(prefix="", tags=["Status"])

@router.get("/status",
            response_model=StatusResponseSchema)
def get_status(db: Session = Depends(get_db)) -> StatusResponseSchema:
    """
    Метод проверки доступности сервиса
    :return: StatusResponseSchema
    """
    return StatusResponseSchema()