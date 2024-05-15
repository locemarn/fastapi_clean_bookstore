import logging

from sqlalchemy import insert

from src.domain.models.user_model import UserModel
from src.domain.repositories.repository_interface import RepositoryInterface
from src.infra.db.database import DatabaseConnection


class UserRepository(RepositoryInterface):
    @classmethod
    def insert(cls, data: dict[str, str]) -> UserModel:
        with DatabaseConnection() as db:
            try:
                if not data['email'] or type(data['email']) is not str:
                    raise TypeError('Email must be a string')

                if not data['password'] or type(data['password']) is not str:
                    raise TypeError('Password must be a string')

                if not data['username'] or type(data['username']) is not str:
                    raise TypeError('Username must be a string')

                new_user = UserModel(
                    email=data['email'],
                    username=data['username'],
                    password=data['password'],
                )

                res = db.session.scalars(
                    insert(UserModel).returning(UserModel),
                    [
                        {
                            'email': new_user.email,
                            'username': new_user.username,
                            'password': new_user.password,
                        }
                    ],
                )
                return res.one()
            except Exception as exception:
                logging.error('UserRepository - insert exception')
                logging.error(exception)
                db.session.rollback()
                raise exception
