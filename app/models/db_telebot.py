from sqlalchemy import JSON, Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models import Base
from app.models.hlp_mixin import SoftDeleteMixin, TimestampMixin


class Telebot(Base, SoftDeleteMixin, TimestampMixin):
    __tablename__ = "telebots"

    id: Mapped[int] = mapped_column(primary_key=True)
    token: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    username: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    description: Mapped[JSON | None] = mapped_column(nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
