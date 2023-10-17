from src.models.configs.connection import DBConnectionHandler
from src.models.configs.base import Base
from src.main.serve import app as application

with DBConnectionHandler() as db:
    engine = db.get_engine()
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000, debug=True)
