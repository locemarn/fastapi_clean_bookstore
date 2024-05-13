from datetime import datetime
from typing import Annotated

from sqlalchemy import String, func
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    validates,
)

timestamp = Annotated[
    datetime,
    mapped_column(nullable=False, server_default=func.CURRENT_TIMESTAMP()),
]


class Base(DeclarativeBase):
    pass


class UserModel(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True, nullable=False
    )
    username: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False
    )
    email: Mapped[str] = mapped_column(String(), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(30), nullable=False)
    created_at: Mapped[timestamp] = mapped_column(
        String,
        nullable=False,
        default=datetime.utcnow,
        server_default=func.now(),
    )
    updated_at: Mapped[timestamp] = mapped_column(
        String,
        nullable=False,
        default=datetime.utcnow,
        server_default=func.now(),
        onupdate=func.now(),
    )

    @classmethod
    @validates('email')
    def validate_email(self, key, address):
        if '@' not in address:
            raise ValueError('failed simple email validation')
        return address

    # def __repr__(self) -> str:
    #     return (
    #         f'<User(id={self.id},'
    #         f'username={self.username},'
    #         f'email={self.email},'
    #         f'password={self.password},'
    #         f'created_at={self.created_at},'
    #         f'updated_at={self.updated_at})>'
    #     )
