from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from typing import Literal
from typing import TypedDict

from fastapi.responses import ORJSONResponse


class SuccessResponse(TypedDict):
    status: Literal["success"]
    data: Any


class ErrorResponse(TypedDict):
    status: Literal["error"]
    data: Any


def success(data: Any) -> ORJSONResponse:
    response_content: SuccessResponse = {
        "status": "success",
        "data": data,
    }

    return ORJSONResponse(content=response_content)


def error(status_code: int, data: Any) -> ORJSONResponse:
    response_content: ErrorResponse = {
        "status": "error",
        "data": data,
    }

    return ORJSONResponse(
        content=response_content,
        status_code=status_code,
    )
