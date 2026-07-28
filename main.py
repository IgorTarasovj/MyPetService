from fastapi import FastAPI

from app.api.status import router as status_router
from app.api.users import router as users_router
from app.db.init_db import init_db


app = FastAPI(
    title="Warehouse Automation API",
    version="1.0",
)

app.include_router(status_router)
app.include_router(users_router)

@app.on_event("startup")
def startup() -> None:
    init_db()


@app.get("/status")
def get_status():
    return {"status": "OK"}
