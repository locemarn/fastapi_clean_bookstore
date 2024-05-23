import logging
from typing import Sequence

from sqlalchemy import delete, insert, select
from sqlalchemy.orm import Session

from src.domain.models.user_model import UserModel
from src.infra.repositories.repository_interface import RepositoryInterface


class InMemoryUserRepository(RepositoryInterface):
    def __init__(self, session: Session) -> None:
        self.__session = session

    def get_all(self) -> Sequence[UserModel]:
        try:
            return self.__session.scalars(select(UserModel)).all()
        except Exception as e:
            logging.exception(e)
            raise e

    def insert(self, item: dict) -> UserModel:
        res = self.__session.scalars(
            insert(UserModel).returning(UserModel),
            [
                {
                    'email': item['email'],
                    'password': item['password'],
                    'username': item['username'],
                }
            ],
        ).one()
        return res

    def delete(self, id: int) -> UserModel:
        res = self.__session.scalars(
            delete(UserModel).where(UserModel.id == id).returning(UserModel)
        ).one_or_none()
        return res
