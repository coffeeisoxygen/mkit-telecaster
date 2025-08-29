"""fast API entri point."""

from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from loguru import logger

from app.config import get_settings
from app.database import DatabaseSessionManager
from app.exception import register_exception_handlers
from app.utils.mlogging.setup import setup_logging

# Setup settings and logging
settings = get_settings()
logconfigpath = Path(__file__).parent.parent / "config_log.yaml"
setup_logging(config_path=logconfigpath, env=settings.APP.environment.value)


# Setup DatabaseSessionManager for lifespan
sessionmanager = DatabaseSessionManager(settings.DB.url)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application starting up.")
    yield
    logger.info("Application shutting down.")
    await sessionmanager.close()


app = FastAPI(
    title=settings.APP.name,
    version=settings.APP.version,
    debug=settings.APP.debug,
    description="aplikasi untuk helper parsing reply addon json yang panjang panjang",
    lifespan=lifespan,
)

# 3. Registrasi exception handler
register_exception_handlers(app)


@app.get("/")
async def root():  # noqa: D103
    return {"message": "Hello World"}
