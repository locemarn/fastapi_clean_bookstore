import logging
import re

from sqlalchemy import insert, select
from sqlalchemy.orm import Session

from src.domain.models.user_model import UserModel
from src.domain.repositories.repository_interface import RepositoryInterface


class UserEntity(RepositoryInterface):
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def insert(self, db: Session):
        try:
            has_user = db.scalars(
                select(UserModel).where(UserModel.email == self.email)
            ).all()

            if has_user:
                raise ValueError(f'User {self.email} already exists')

            new_user = UserModel(
                username=self.username,
                email=self.email,
                password=self.password,
            )
            print('new_user', new_user)
            db.execute(
                insert(UserModel).returning(UserModel), [new_user.__dict__]
            )
            return {'user': new_user.__dict__}
        except Exception as e:
            logging.error('create_user entity exception')
            logging.error(e)
            db.rollback()
            raise e

    @classmethod
    def __is_valid_email(cls, value) -> str | None:
        regex = re.compile(
            r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
        )
        r = re.fullmatch(regex, value)
        return r

    @property
    def username(self):
        return self._username

    @property
    def email(self):
        return self._email

    @property
    def password(self):
        return self._password

    @username.setter
    def username(self, value):
        if type(value) is not str:
            raise TypeError('username must be a string')

        if not str(value):
            raise ValueError('username cannot be empty')

        self._username = value

    @email.setter
    def email(self, value):
        if type(value) is not str:
            raise TypeError('Email must be a string')

        if not str(value):
            raise ValueError('Email cannot be empty')

        if not self.__is_valid_email(value):
            raise ValueError('Invalid email address')

        self._email = value

    @password.setter
    def password(self, value):
        if type(value) is not str:
            raise TypeError('Password must be a string')

        if not str(value):
            raise ValueError('Password cannot be empty')

        self._password = value
