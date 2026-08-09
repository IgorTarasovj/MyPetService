from sqlalchemy import text

from src.db.db_client import DatabaseClient
from src.schemas.users.user import User

class UserRepository:

    def __init__(self, db_client: DatabaseClient):
        self.db_client  = db_client

    def get_default_user_id(self):
        query = text("""
                  SELECT id
                  FROM users
                  WHERE username = 'admin'
              """)

        user_id = self.db_client.session.scalar(query)

        return user_id

