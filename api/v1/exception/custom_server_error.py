from starlette import status


class CustomException(Exception):
    def __init__(self, message: str):
        self.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        self.message = message
