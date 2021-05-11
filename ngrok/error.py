from typing import Any, Optional


class Error(Exception):
    """Raised by failed ngrok API operations.

    This class encapsulates details about the error to make it simple for callers
    to introspect the error and take action on it.

    :param error_code: The unique ngrok error code indicating why the operation failed.
    :param message: Human-readable string explaining the error.
    :param http_status_code: HTTP status code returned by the server.
    :param details: Arbitrary additional details about the error.
    """

    def __init__(
        self,
        error_code: Optional[int],
        message: str,
        http_status_code: int,
        details: Any,
    ):
        super().__init__(self, message)
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.details = details


class NotFoundError(Error):
    """Raised if the http_status_code of an API operation is 404.
    This is a separate class to make this common condition easier to handle.
    """

    pass
