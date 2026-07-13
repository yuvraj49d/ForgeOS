import time

from fastapi import Request

from app.shared.logger import setup_logger

logger = setup_logger()


async def request_logging_middleware(request: Request, call_next):
    """
    Logs every incoming request and outgoing response.
    """

    start_time = time.perf_counter()

    response = await call_next(request)

    process_time = (time.perf_counter() - start_time) * 1000

    logger.info(
        "%s %s %s %.2f ms",
        request.method,
        request.url.path,
        response.status_code,
        process_time,
    )

    return response