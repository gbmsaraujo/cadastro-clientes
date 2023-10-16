from src.controllers.interface.Icadastro_controller import ICadastroController
from src.views.types_view.http_request import HttpRequest
from src.views.types_view.http_response import HttpResponse


class CadastroView:
    def __init__(self, cadastro_controller: ICadastroController) -> None:
        self.__controller = cadastro_controller

    def cadastrar_view(self, req: HttpRequest) -> HttpResponse:
        client = req.body
        try:
            response = self.__controller.cadastrar_pessoa(client)

            if response:
                return self.__convert_to_dict(HttpResponse(200, response))

        except Exception as exception:
            return self.__convert_to_dict(HttpResponse(400, str(exception)))

    def buscar_view(self, req: HttpRequest) -> HttpResponse:
        nome = req.body["nome"]

        try:
            response = self.__controller.buscar_pessoa_por_nome(nome)

            if not response:
                self.__convert_to_dict(
                    HttpResponse(200, "Não há usuários com esse nome")
                )

            return self.__convert_to_dict(HttpResponse(200, response.__dict__))

        except Exception as exception:
            return self.__convert_to_dict(HttpResponse(400, str(exception)))

    def deletar_view(self, req: HttpRequest) -> HttpResponse:
        nome = req.body["nome"]

        try:
            response = self.__controller.deletar_pessoa_pelo_nome(nome)

            if not response:
                return self.__convert_to_dict(
                    HttpResponse(200, "Não há usuários para deletar")
                )
            return self.__convert_to_dict(
                HttpResponse(200, "Usuário deletado com sucesso")
            )
        except Exception as exception:
            return self.__convert_to_dict(HttpResponse(400, str(exception)))

    def atualizar_view(self, req: HttpRequest) -> HttpResponse:
        info_client = req.body

        try:
            response = self.__controller.alterar_cadastro(info_client)

            if not response:
                return self.__convert_to_dict(
                    HttpResponse(200, "Não há usuários para atualizar")
                )
            return self.__convert_to_dict(
                HttpResponse(200, "Usuário atualizado com sucesso")
            )
        except Exception as exception:
            return self.__convert_to_dict(HttpResponse(400, str(exception)))

    def __convert_to_dict(obj_response):
        return obj_response.__dict__
