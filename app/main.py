"""fast API entri point."""

from fastapi import FastAPI

from app.exception import register_exception_handlers

app = FastAPI()

register_exception_handlers(app)
