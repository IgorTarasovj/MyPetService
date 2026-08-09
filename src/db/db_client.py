from sqlalchemy import create_engine
from sqlalchemy.orm import Session

class DatabaseClient:
    def __init__(self, database_url: str):
        self.engine = create_engine(database_url)
        self.session = Session(bind=self.engine)

    def close(self):
        self.session.close()