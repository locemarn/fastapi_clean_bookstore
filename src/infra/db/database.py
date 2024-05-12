from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from src.infra.db.settings import Settings


class DatabaseConnection:
    def __init__(self):
        self.__connection_string = Settings().DATABASE_URL
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        with Session(self.__engine) as session:
            yield session
        # return self.__engine

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
