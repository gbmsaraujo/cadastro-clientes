from abc import ABC, abstractmethod
from typing import List
from src.models.types.cadastro_type import CadastroType


class ICadastroRepo(ABC):
    @abstractmethod
    def get_clients(self) -> List[CadastroType]:
        pass

    @abstractmethod
    def search_client_by_name(self, name: str) -> CadastroType or None:
        pass

    @abstractmethod
    def delete_client_by_name(self, name: str) -> bool:
        pass

    @abstractmethod
    def update_info_person(self, name: str, info_client: CadastroType) -> bool:
        pass

    @abstractmethod
    def insert_client(self, info_client: CadastroType) -> bool:
        pass
