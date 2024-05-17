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


# @event.listens_for(UserModel, 'init_scalar', retval=True, propagate=True)
# def before_insert(target, dict_, value):
#     print('instance', target)
#     print('instance', dict_)
#
#     print('instance', value)

# to_validate_data = {
#     'username': instance.username,
#     'email': instance.email,
#     'password': instance.password,
# }
# user_insert_validator(to_validate_data)
