from flask  import Blueprint, request, jsonify

app_routes_bp = Blueprint("api_routes", __name__)


@app_routes_bp.route('/')
def index():
    return "Hello World!"

@app_routes_bp.route("/cadastro", methods=["POST"])
def cadastro():
    payload = request.json
    print(payload)

    return "Ok"