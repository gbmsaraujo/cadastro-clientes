class HttpNotFoundError(Exception):
    """Class to generate Not found 404 Http

    :param Exception: _description_
    :type Exception: _type_
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = "NotFound"
        self.status_code = 404
