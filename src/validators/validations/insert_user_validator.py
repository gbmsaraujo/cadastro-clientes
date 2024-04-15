from cerberus import Validator

body_validator = Validator(
    {
        "nome": {"type": "string", "required": True, "empty": False},
        "idade": {"type": "float", "required": False, "empty": False},
        "bairro": {"type": "string", "required": True, "empty": True},
        "profissao": {"type": "string", "required": False, "empty": False},
    }
)
