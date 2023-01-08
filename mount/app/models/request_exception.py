from typing import Any


class RequestException(Exception):
    def __init__(self, response: Any, status_code: int) -> None:
        self.response = response
        self.status_code = status_code
