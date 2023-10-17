from src.controllers.cadastro_controller import CadastroController
from src.models.repositories.cadastro_repository import CadastroRepository
from src.views.cadastro_view import CadastroView

def cadastro_compose():
    cadastro_db = CadastroRepository()
    cadastro_controller = CadastroController(cadastro_db)
    cadastro_view = CadastroView(cadastro_controller)

    return cadastro_view