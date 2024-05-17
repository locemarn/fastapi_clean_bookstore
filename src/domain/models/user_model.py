from datetime import datetime
from typing import Annotated

from sqlalchemy import Integer, String, func
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
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
        Integer, primary_key=True, autoincrement=True, nullable=False
    )
    username: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False
    )
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
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

    # @classmethod
    # @validates('email')
    # def validate_email(cls, key, address):
    #     print('key', key)
    #     print('address', address)
    #
    #     if '@' not in address:
    #         raise ValueError('failed simple email validation')
    #     return address


# @classmethod
# @validates('email')
# def validate_email(cls, key, email: str):
#     print('email', email)
#     if not email or type(email) is not str:
#         raise ValueError('Username cannot be empty')
#     return email.strip()
#
#
# @event.listens_for(UserModel, 'before_insert')
# def before_insert(mapper, connection, target):
#     print('akiiiiiii', type(target.username) is not str)
#     if not target.username or type(target.username) is not str:
#         print('akiiiiiii')
#         raise ValueError('Username cannot be empty 2')
#
#     print('mapper', mapper)
#     print('connection', connection)
#     print('target', target)
