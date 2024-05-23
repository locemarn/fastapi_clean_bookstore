import logging
from typing import List

from sqlalchemy import insert

from src.domain.models.user_model import UserModel
from src.infra.db.database import DatabaseConnection
from src.infra.repositories.repository_interface import RepositoryInterface


class UserRepository(RepositoryInterface):
    @classmethod
    def get_all(cls) -> List[UserModel]:
        with DatabaseConnection() as db:
            try:
                result = db.session.query(UserModel)
                return result.all()
            except Exception as exception:
                logging.error('UserRepository - get_all exception')
                logging.error(exception)
                db.session.rollback()
                raise exception

    @classmethod
    def insert(cls, item: dict) -> UserModel:
        with DatabaseConnection() as db:
            try:
                email = item['email']
                password = item['password']
                username = item['username']

                res = db.session.scalars(
                    insert(UserModel).returning(UserModel),
                    [
                        {
                            'email': email,
                            'password': password,
                            'username': username,
                        }
                    ],
                ).one()
                db.session.commit()
                db.session.refresh(res)
                return res
            except Exception as exception:
                logging.error('UserRepository - insert exception')
                logging.error(exception)
                db.session.rollback()
                raise exception

    @classmethod
    def delete(cls, id: int) -> UserModel:
        with DatabaseConnection() as db:
            try:
                res = (
                    db.session.query(UserModel)
                    .filter(UserModel.id == id)
                    .one_or_none()
                )
                db.session.delete(res)
                db.session.commit()
                return res
            except Exception as exception:
                logging.error('UserRepository - delete exception')
                logging.error(exception)
                db.session.rollback()
                raise exception
