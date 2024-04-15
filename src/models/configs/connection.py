from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.constants.constants import DATABASE_NAME, HOST_DB, PASSWORD_DB, USER_DB


class DBConnectionHandler:

    def __init__(self) -> None:
        self.__connection_string = (
            f"mysql+pymysql://{USER_DB}:{PASSWORD_DB}@{HOST_DB}/{DATABASE_NAME}"
        )

        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
