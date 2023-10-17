from src.controllers.interface.Icadastro_controller import ICadastroController
from src.views.types_view.http_request import HttpRequest
from src.views.types_view.http_response import HttpResponse


class CadastroView:
    def __init__(self, cadastro_controller: ICadastroController) -> None:
        self.__controller = cadastro_controller

    def cadastrar_view(self, http_request: HttpRequest) -> HttpResponse:
        client = http_request.body

        try:
            response = self.__controller.cadastrar_pessoa(client)

            if response:
                return HttpResponse(200, response).__dict__

        except Exception as exception:
            return HttpResponse(400, str(exception)).__dict__

    def buscar_view(self, http_request: HttpRequest) -> HttpResponse:
        nome = http_request.body["nome"].lower()

        try:
            response = self.__controller.buscar_pessoa_por_nome(nome)

            if not response:
                (HttpResponse(200, "Não há usuários com esse nome")).__dict__

            return HttpResponse(
                200,
                {
                    "nome": response["nome"],
                    "bairro": response["bairro"],
                    "idade": response["idade"],
                    "profissao": response["profissao"],
                },
            ).__dict__

        except Exception as exception:
            return HttpResponse(400, str(exception)).__dict__

    def deletar_view(self, http_request: HttpRequest) -> HttpResponse:
        nome = http_request.body["nome"]

        try:
            response = self.__controller.deletar_pessoa_pelo_nome(nome)

            if not response:
                return HttpResponse(200, "Não há usuários para deletar").__dict__
            return HttpResponse(200, "Usuário deletado com sucesso").__dict__

        except Exception as exception:
            return HttpResponse(400, str(exception)).__dict__

    def atualizar_view(self, http_request: HttpRequest) -> HttpResponse:
        info_client = http_request.body

        try:
            response = self.__controller.alterar_cadastro(info_client)

            if not response:
                return HttpResponse(200, "Não há usuários para atualizar").__dict__
            return HttpResponse(200, "Usuário atualizado com sucesso").__dict__
        except Exception as exception:
            return HttpResponse(400, str(exception)).__dict__

    def __convert_to_dict(obj_response):
        return obj_response.__dict__



# Duvidas:
    # Como devolver uma resposta? Tirar o dict
    # Mostrar o erro do buscar view se devolvemos direto o response ao invés do dicionario