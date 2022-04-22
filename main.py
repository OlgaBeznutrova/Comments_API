import uvicorn

from conf.settings import settings

uvicorn.run(
    "fastapi_app:app",
    host=settings.fst_host,
    port=settings.fst_port
)
