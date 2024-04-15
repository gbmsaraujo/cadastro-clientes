from src.errors.types.http_not_found import HttpNotFoundError
from src.errors.types.http_unprocessable_entity_error import HttpUnprocessableEntityError


def handle_errors(error: Exception) -> dict:
    """
    Handle  to treat Exception Cases

    :param error: Exception
    :type error: Exception
    :return: Dict with data and status_code
    """

    if isinstance(error, HttpNotFoundError):
        return {"data": {"error": error.message}, "status_code": error.status_code}
    
    if isinstance(error, HttpUnprocessableEntityError):
        return {"data": {"error": error.message}, "status_code": error.status_code}


    return {"data": {"error": str(error)}, "status_code": 500}
