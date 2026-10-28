from datetime import datetime

from sqlalchemy import DateTime, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Service(Base):
    __tablename__ = "services"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    slug: Mapped[str] = mapped_column(String(120), index=True)
    owner: Mapped[str] = mapped_column(String(120))
    env: Mapped[str] = mapped_column(String(120))
    status: Mapped[str] = mapped_column(String(40), default="healthy")
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
