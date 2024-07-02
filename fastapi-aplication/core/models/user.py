# Привер создании базы данных

from .base import Base
from sqlalchemy.orm import mapped_column, Mapped

class User(Base):
    username: Mapped[str] = mapped_column(unique=True)