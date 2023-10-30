from flask import Blueprint, request, jsonify
from src.main.composer.cadastro_compose import cadastro_compose
from src.main.adapter.request_adapter import request_adapter
from src.validators.insert_user_validator import body_validator
from src.errors.handle_errors import handle_errors
from src.errors.types.http_unprocessable_entity_error import (
    HttpUnprocessableEntityError,
)
from src.validators.user_name_validator import user_name_validator

app_routes_bp = Blueprint("api_routes", __name__)


@app_routes_bp.route("/")
def index():
    return "Hello World!"


@app_routes_bp.route("/cadastro", methods=["POST"])
def cadastro():
    http_request = request_adapter(request)
    validator = body_validator.validate(http_request.body)

    if not validator:
        raise HttpUnprocessableEntityError(
            message="Erro ao processar o body, verifique os parâmetros enviados"
        )

    response = cadastro_compose().cadastrar_view(http_request)

    return response


@app_routes_bp.route("/delete", methods=["PUT"])
def delete():
    http_request = request_adapter(request)
    validator = user_name_validator.validate(http_request.body)

    if not validator:
        raise HttpUnprocessableEntityError(
            message="Erro ao processar o body, verifique os parâmetros enviados"
        )

    response = cadastro_compose().deletar_view(http_request)

    return response


@app_routes_bp.route("/pesquisar", methods=["POST"])
def pesquisa():
    http_request = request_adapter(request)
    validator = user_name_validator.validate(http_request.body)

    if not validator:
        raise HttpUnprocessableEntityError(
            message="Erro ao processar o body, verifique os parâmetros enviados"
        )
    response = cadastro_compose().buscar_view(http_request)
    return response


@app_routes_bp.route("/atualizar", methods=["POST"])
def atualizar():
    http_request = request_adapter(request)
    validator = body_validator.validate(http_request.body)

    if not validator:
        raise HttpUnprocessableEntityError(
            message="Erro ao processar o body, verifique os parâmetros enviados"
        )

    response = cadastro_compose().atualizar_view(http_request)
    return response
