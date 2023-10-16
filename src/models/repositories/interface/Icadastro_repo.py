from abc import ABC, abstractmethod
from typing import List, Dict
from src.models.repositories.types.pessoas_type import PessoaType
from src.controllers.types_controller.cadastro_types import PessoaController

class ICadastroRepo(ABC):

    @abstractmethod
    def get_clients(self) -> List[PessoaType]:
        pass

    @abstractmethod
    def search_client_by_name(self, name: str) -> PessoaType or None:
        pass

    @abstractmethod
    def delete_client_by_name(self, name: str) -> bool:
        pass

    @abstractmethod
    def update_info_person(self, name: str, age: int, profession: str, neighborhood: str) -> bool:
        pass

    @abstractmethod
    def insert_client(self, pessoa: PessoaController) -> bool:
        pass