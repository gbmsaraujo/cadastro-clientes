from cerberus import Validator

user_name_validator = Validator(
    {
        "nome": {"type": "string", "required": True, "empty": False},
    }
)
