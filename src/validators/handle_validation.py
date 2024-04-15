from cerberus import Validator
from src.errors.types.http_unprocessable_entity_error import HttpUnprocessableEntityError

def handle_validations(validator:Validator, data: dict):
    validate_data = validator.validate(data)

    if not validate_data:
        raise HttpUnprocessableEntityError(
            message="Erro ao processar o body, verifique os parâmetros enviados"
        )