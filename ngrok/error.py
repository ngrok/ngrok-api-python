from typing import Any, Optional

class ValidationError(Exception):
    def __init__(self, error_code: Optional[int], message: str, status_code: int, details: Any):
        super().__init__(self, message)
        self.error_code = error_code
        self.status_code = status_code
        self.details = details
