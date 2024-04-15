import os
from dotenv import load_dotenv

load_dotenv()

USER_DB = os.getenv("USER_DB")
PASSWORD_DB = os.getenv("PASSWORD_DB")
HOST_DB = os.getenv("HOST_DB")
DATABASE_NAME = os.getenv("DATABASE_NAME")
