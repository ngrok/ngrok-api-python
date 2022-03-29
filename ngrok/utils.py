from typing import Any, Optional


def extract_props(value: Optional[Any]) -> Any:
    if value:
        return value._props
    return None
