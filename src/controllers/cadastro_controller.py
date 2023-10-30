from src.models.repositories.interface.Icadastro_repo import ICadastroRepo
from src.controllers.interface.Icadastro_controller import ICadastroController
from src.models.types.cadastro_type import CadastroType
from src.views.types_view.http_response import HttpResponse
from src.errors.types.http_not_found import HttpNotFoundError


class CadastroController(ICadastroController):
    def __init__(self, cadastro_db: ICadastroRepo):
        self.cadastro_db = cadastro_db

    def cadastrar_pessoa(self, pessoa: CadastroType) -> HttpResponse:
        self.cadastro_db.insert_client(pessoa)
        return self.__format_response(
            person=pessoa, status_code=201, message="Cadastro Realizado Com Sucesso"
        )

    def buscar_pessoa_por_nome(self, nome: str):
        query = self.cadastro_db.search_client_by_name(nome)

        if not query:
            raise HttpNotFoundError(message="Nenhuma Pessoa Foi Encontrada no Banco")

        return self.__format_response(person=query.__dict__, status_code=201)

    def deletar_pessoa_pelo_nome(self, nome: str) -> HttpResponse:
        query = self.cadastro_db.delete_client_by_name(nome)

        if not query:
            raise HttpNotFoundError(message="Nenhuma Pessoa Foi Encontrada no Banco")

        return self.__format_response(
            status_code=204, message="Pessoa deletada com sucesso"
        )

    def alterar_cadastro(self, info_client: CadastroType) -> HttpResponse:
        query = self.cadastro_db.update_info_person(info_client)

        if not query:
            raise HttpNotFoundError(message="Nenhuma Pessoa Foi Encontrada no Banco")

        return self.__format_response(
            status_code=204,
            message="Atualização Realizada Com Sucesso",
            person=query.__dict__,
        )

    def __format_response(
        self, person: CadastroType = {}, status_code: int = 200, message: str = ""
    ):
        return {
            "status_code": status_code,
            "message": message,
            "response"
            if person
            else None: {
                "nome": person.nome,
                "idade": person.idade,
                "bairro": person.bairro,
                "profissão": person.profissao,
            },
        }
