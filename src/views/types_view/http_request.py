
class HttpRequest:

    def __init__(
        self,
        header: dict = None,
        body: dict = None,
        query_params: dict = None,
        url: str = None,
        token_information: dict = None
    ):
        self.header = header
        self.body = body
        self.query_params = query_params
        self.url = url
        self.token_information = token_information
