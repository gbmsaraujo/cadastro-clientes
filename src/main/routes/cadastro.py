from flask import Blueprint, request, jsonify
from src.main.composer.cadastro_compose import cadastro_compose
from src.main.adapter.request_adapter import request_adapter
from src.errors.handle_errors import handle_errors



app_routes_bp = Blueprint("api_routes", __name__)


@app_routes_bp.route("/")
def index():
    return "Hello to register clients!"


@app_routes_bp.route("/cadastro", methods=["POST"])
def cadastro():
    http_request = request_adapter(request)

    response = cadastro_compose().cadastrar_view(http_request)

    return response


@app_routes_bp.route("/delete", methods=["PUT"])
def delete():
    http_request = request_adapter(request)

    response = cadastro_compose().deletar_view(http_request)

    return response


@app_routes_bp.route("/pesquisar", methods=["POST"])
def pesquisa():
    http_request = request_adapter(request)

    response = cadastro_compose().buscar_view(http_request)

    return response


@app_routes_bp.route("/atualizar", methods=["POST"])
def atualizar():
    http_request = request_adapter(request)

    response = cadastro_compose().atualizar_view(http_request)

    return response
