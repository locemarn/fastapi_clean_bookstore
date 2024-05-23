from src.domain.entities.user_entity import UserEntity
from src.domain.models.user_model import UserModel


class InsertUserUseCase:
    def __init__(self, entity: UserEntity):
        self.__entity = entity

    def execute(self, user: dict) -> UserModel:
        return self.__entity.insert_user(user)
