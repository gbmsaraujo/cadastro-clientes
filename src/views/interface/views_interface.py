from abc import ABC, abstractmethod
from src.views.types_view.http_response import HttpResponse


class ViewsInterface(ABC):
    @abstractmethod
    def cadastrar_view(self) -> HttpResponse:
        pass

    @abstractmethod
    def buscar_view(self) -> HttpResponse:
        pass

    @abstractmethod
    def deletar_view(self) -> HttpResponse:
        pass

    @abstractmethod
    def atualizar_view(self) -> HttpResponse:
        pass
