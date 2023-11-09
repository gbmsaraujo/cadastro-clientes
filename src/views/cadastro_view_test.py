from src.models.types.cadastro_type import CadastroType
from src.views.types_view.http_response import HttpResponse
from src.errors.types.http_not_found import HttpNotFoundError


pessoa_mock = (
    {
        "nome": "gabriel",
        "idade": 30,
        "bairro": "Maracanã",
        "profissão": "Programador",
    },
)

class MockCadastroController:
    def cadastrar_pessoa(self, pessoa: CadastroType) -> HttpResponse:
        return {
            "status_code": 201,
            "message": "Cadastro Realizado Com Sucesso",
            "response": {
                "nome": pessoa["nome"],
                "idade": pessoa["idade"],
                "bairro": pessoa["bairro"],
                "profissão": pessoa["profissao"],
            },
        }

    def buscar_pessoa_por_nome(self, nome, person: CadastroType) -> HttpResponse:
        if not nome == person["nome"]:
            raise HttpNotFoundError(message="Nenhuma Pessoa Foi Encontrada no Banco")

        return {
            "status_code": 201,
            "message": "Cadastro Realizado Com Sucesso",
            "response": {
                "nome": person["nome"],
                "idade": person["idade"],
                "bairro": person["bairro"],
                "profissão": person["profissao"],
            },
        }

    def deletar_pessoa_pelo_nome(self, nome: str, person: CadastroType) -> HttpResponse:
        if not nome == person["nome"]:
            raise HttpNotFoundError(message="Nenhuma Pessoa Foi Encontrada no Banco")
        
        return {
            "status_code": 201,
            "message": "Cadastro Realizado Com Sucesso",
            "response": "Pessoa deletada com sucesso"
        }


    def alterar_cadastro(self, pessoa: CadastroType) -> HttpResponse:
        pass
