class HttpResponse:
    def __init__(self, status_code, response) -> None:
        self.status_code = status_code
        self.response = response