from src.controllers.types_controller.cadastro_types import CadastroType
from models.repositories.interface.Icadastro_repo import ICadastroRepo
from src.models.repositories.interface.Icadastro_repo import ICadastroRepo
from src.controllers.interface.Icadastro_controller import ICadastroController


class CadastroController(ICadastroController):
    def __init__(self, cadastro_db: ICadastroRepo) -> None:
        self.cadastro_db = cadastro_db

    def cadastrar_pessoa(self, pessoa: CadastroType):
        try:
            self.cadastro_db.insert_client(pessoa)
            return "Pessoa cadastrada com sucesso!"
        except:
            return "Erro ao cadastrar pessoa!"

    def buscar_pessoa_por_nome(self, nome: str):
        query = self.cadastro_db(nome)

        return query

    def deletar_pessoa_pelo_nome(self, nome: str):
        query = self.cadastro_db.delete_client_by_name(nome)

        return query

    def alterar_cadastro(self, info_cliente: CadastroType):
        query = self.cadastro_db.update_info_person(info_cliente)

        return query
