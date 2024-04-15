from .cadastro_controller import CadastroController
from src.models.entities.pessoas import PessoaEntity
from src.errors.types.http_not_found import HttpNotFoundError


class SpyCadastroRepo:
    def __init__(self) -> None:
        self.search_client_by_name_attribute = {}

    def search_client_by_name(self, name: str) -> PessoaEntity:
        self.search_client_by_name_attribute["name"] = name
        return PessoaEntity(
            id=123,
            nome="ze da manga",
            idade=10,
            bairro="something",
            profissao="algumacoisa",
        )


class SpyCadastroRepoNotFoundError:
    def __init__(self) -> None:
        self.search_client_by_name_attribute = {}

    def search_client_by_name(self, name: str) -> PessoaEntity:
        self.search_client_by_name_attribute["name"] = name
        return None


def test_buscar_pessoa_por_nome():
    mock_name = "olaMundo"

    repo = SpyCadastroRepo()
    controller = CadastroController(repo)

    response = controller.buscar_pessoa_por_nome(mock_name)

    assert repo.search_client_by_name_attribute["name"] == mock_name

    assert isinstance(response, dict)
    assert "status_code" in response
    assert isinstance(response["status_code"], int)
    assert "response" in response
    assert isinstance(response["response"], dict)

    assert "nome" in response["response"]


def test_buscar_pessoa_por_nome_not_found():
    mock_name = "olaMundo"

    repo = SpyCadastroRepoNotFoundError()
    controller = CadastroController(repo)

    try:
        controller.buscar_pessoa_por_nome(mock_name)
        assert False
    except Exception as exception:
        assert repo.search_client_by_name_attribute["name"] == mock_name
        assert isinstance(exception, HttpNotFoundError)
        assert str(exception) == "Nenhuma Pessoa Foi Encontrada no Banco"
