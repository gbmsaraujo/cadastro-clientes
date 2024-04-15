from abc import ABC, abstractmethod
from src.models.types.cadastro_type import CadastroType
from src.views.types_view.http_response import HttpResponse


class ICadastroController(ABC):
    @abstractmethod
    def cadastrar_pessoa(self, pessoa: CadastroType) -> HttpResponse:
        pass

    @abstractmethod
    def buscar_pessoa_por_nome(self, nome: str) -> HttpResponse:
        pass

    @abstractmethod
    def deletar_pessoa_pelo_nome(self, nome: str) -> HttpResponse:
        pass

    @abstractmethod
    def alterar_cadastro(self, pessoa: CadastroType) -> HttpResponse:
        pass
