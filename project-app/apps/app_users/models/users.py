from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from core.db.model import Base


class User(Base):
    username: Mapped[str] = mapped_column(unique=True)
    foo: Mapped[int]
    bar: Mapped[int]

    # __table_args__ = (UniqueConstraint('foo', 'bar'),)  # noqa: ERA001
