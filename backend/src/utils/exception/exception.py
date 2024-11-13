from starlette.responses import JSONResponse


async def custom_http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": str(exc)},
    )

async  def custom_requestvalueError_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": str(exc)},
    )
