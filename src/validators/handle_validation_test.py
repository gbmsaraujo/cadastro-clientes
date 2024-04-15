from cerberus import Validator
from src.errors.types.http_unprocessable_entity_error import (
    HttpUnprocessableEntityError,
)


mock_validator = Validator(
    {
        "nome": {"type": "string", "required": True, "empty": False},
        "idade": {"type": "float", "required": False, "empty": False},
        "bairro": {"type": "string", "required": True, "empty": True},
        "profissao": {"type": "string", "required": False, "empty": False},
    }
)


def test_handle_validation():
    data = {
        "nome": "Gabriel",
        "idade": 30,
        "bairro": "Riachuelo",
        "profissao": "Programador",
    }

    validate_data = mock_validator.validate(data)

    assert validate_data is True


def test_error_handle_validation():
    data = {}

    try:
        validate_data = mock_validator.validate(data)
    except Exception as exception:
        assert isinstance(exception, HttpUnprocessableEntityError)
        assert (
            str(exception)
            == "Erro ao processar o body, verifique os parâmetros enviados"
        )
