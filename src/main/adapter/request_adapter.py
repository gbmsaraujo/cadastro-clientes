from flask import request as FlaskRequest
from src.views.types_view.http_request import HttpRequest


def request_adapter(request: FlaskRequest):
    http_request = HttpRequest(
        headers=request.headers,
        body=request.json,
        query_params=request.args,
        url=request.full_path,
    )

    return http_request
