from abc import ABC, abstractmethod
from src.models.types.cadastro_type import CadastroType


class ICadastroController(ABC):
    @abstractmethod
    def cadastrar_pessoa(self, pessoa: CadastroType):
        pass

    @abstractmethod
    def buscar_pessoa_por_nome(self, nome: str):
        pass

    @abstractmethod
    def deletar_pessoa_pelo_nome(self, nome: str):
        pass

    @abstractmethod
    def alterar_cadastro(self, pessoa: CadastroType):
        pass
