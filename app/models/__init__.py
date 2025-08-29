from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


from app.models.db_user import User
from app.models.db_telebot import Telebot

__all__ = ["User", "Telebot"]
