from src.models.repositories.interface.Icadastro_repo import ICadastroRepo
from src.controllers.interface.Icadastro_controller import ICadastroController
from src.models.types.cadastro_type import CadastroType


class CadastroController(ICadastroController):
    def __init__(self, cadastro_db: ICadastroRepo) -> None:
        self.cadastro_db = cadastro_db

    def cadastrar_pessoa(self, pessoa: CadastroType):
        try:
            self.cadastro_db.insert_client(pessoa)
            return "Pessoa cadastrada com sucesso!"
        except ValueError as error:
            return error

    def buscar_pessoa_por_nome(self, nome: str):
        print(nome)
        query = self.cadastro_db.search_client_by_name(nome)

        return query

    def deletar_pessoa_pelo_nome(self, nome: str):
        query = self.cadastro_db.delete_client_by_name(nome)

        return query

    def alterar_cadastro(self, info_client: CadastroType):
        query = self.cadastro_db.update_info_person(info_client)

        return query
