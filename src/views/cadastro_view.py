from src.controllers.interface.Icadastro_controller import ICadastroController
from src.views.types_view.http_request import HttpRequest
from src.views.types_view.http_response import HttpResponse
from src.validators.handle_validation import handle_validations
from src.validators.validations.user_name_validator import user_name_validator
from src.validators.validations.insert_user_validator import body_validator


class CadastroView:
    def __init__(self, cadastro_controller: ICadastroController) -> None:
        self.__controller = cadastro_controller

    def cadastrar_view(self, http_request: HttpRequest) -> HttpResponse:
        try:
            handle_validations(body_validator, http_request.body)
            response = self.__controller.cadastrar_pessoa(http_request.body)

            return response

        except Exception as exception:
            return str(exception)

    def buscar_view(self, http_request: HttpRequest) -> HttpResponse:
        try:
            handle_validations(user_name_validator, http_request.body)
            nome = http_request.body["nome"].lower()

            response = self.__controller.buscar_pessoa_por_nome(nome)

            return response

        except Exception as exception:
            return str(exception)

    def deletar_view(self, http_request: HttpRequest) -> HttpResponse:
        try:
            handle_validations(user_name_validator, http_request.body)
            nome = http_request.body["nome"].lower()
            response = self.__controller.deletar_pessoa_pelo_nome(nome)

            return response

        except Exception as exception:
            return str(exception)

    def atualizar_view(self, http_request: HttpRequest) -> HttpResponse:
        try:
            handle_validations(body_validator, http_request.body)
            info_client = http_request.body
            response = self.__controller.alterar_cadastro(info_client)

            return response
        except Exception as exception:
            return str(exception)


# Duvidas:
# Como devolver uma resposta? Tirar o dict
# Mostrar o erro do buscar view se devolvemos direto o response ao invés do dicionario
