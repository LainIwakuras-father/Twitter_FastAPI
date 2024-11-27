from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi.requests import Request


class CustomException(HTTPException):
    """
    Кастомная ошибка для быстрого вызова исключений
    """
    pass


async def custom_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    """
    Кастомный обработчик ошибок для CustomApiException
    """
    return JSONResponse(
        {
            "result": False,
            "error_type": f"{exc.status_code}",
            "error_message": str(exc.detail),
        },
        status_code=exc.status_code,
    )