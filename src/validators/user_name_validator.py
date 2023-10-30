from cerberus import Validator

user_name_validator = Validator({
    "data": {
        "type": "dict",
        "schema": {
            "nome": { "type": "string", "required": True, "empty": False },
        }
    },
})

