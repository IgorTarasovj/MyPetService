from fastapi import FastAPI

from app.api.status import router as status_router

app = FastAPI(
    title="Warehouse Automation API",
    version="1.0",
)

app.include_router(status_router)