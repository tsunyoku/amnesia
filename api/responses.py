from msilib.schema import Error
from typing import TypedDict, Generic, TypeVar, Literal

T = TypeVar("T")


class SuccessResponse(TypedDict, Generic[T]):
    status: Literal["success"]
    data: T


class ErrorResponse(TypedDict, Generic[T]):
    status: Literal["error"]
    data: T


APIResponse = SuccessResponse[T] | ErrorResponse[T]


def success(data: T) -> SuccessResponse[T]:
    return {
        "status": "success",
        "data": data,
    }


def error(data: T) -> ErrorResponse[T]:
    return {
        "status": "error",
        "data": data,
    }
