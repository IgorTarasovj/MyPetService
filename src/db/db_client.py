from sqlalchemy import create_engine
from sqlalchemy.orm import Session

class DatabaseClient:
    def __init__(self, database_url: str):
        """
        Базовый клиент подключения к базе данных по url
        :param database_url: url базы данных
        """
        self.engine = create_engine(database_url)
        self.session = Session(bind=self.engine)

    def close(self):
        """
        Метод, закрывающий соединение к базе данных
        """
        self.session.close()