from typing import List

from src.domain.models.user_model import UserModel
from src.infra.repositories.repository_interface import RepositoryInterface


class UserEntity:
    def __init__(self, repository: RepositoryInterface) -> None:
        self.__repository = repository

    def get_all_users(self) -> List[UserModel]:
        return self.__repository.get_all()

    def insert_user(self, user: dict) -> UserModel:
        return self.__repository.insert(user)

    def delete_user(self, user_id: int) -> UserModel:
        return self.__repository.delete(user_id)
