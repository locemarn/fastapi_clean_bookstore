from typing import List

from src.domain.entities.user_entity import UserEntity
from src.domain.models.user_model import UserModel


class GetAllUsersUseCase:
    # def __init__(self, db):
    #     self.__db = db

    def __init__(self, entity: UserEntity):
        self.__entity = entity

    def execute(self) -> List[UserModel]:
        # user_entity = UserEntity(self.__db)
        # return user_entity.get_all_users()
        return self.__entity.get_all_users()
