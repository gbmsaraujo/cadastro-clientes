from src.controllers.cadastro_controller import CadastroController
from src.models.repositories.cadastro_repository import CadastroRepository

def cadastro_compose():
    cadastro_db = CadastroRepository()
    cadastro_controller = CadastroController(cadastro_db)
    cadastro_view = ""