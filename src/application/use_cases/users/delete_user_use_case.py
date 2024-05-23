from src.domain.entities.user_entity import UserEntity
from src.domain.models.user_model import UserModel


class DeleteUserUseCase:
    def __init__(self, entity: UserEntity):
        self.__entity = entity

    def execute(self, user_id: int) -> UserModel:
        return self.__entity.delete_user(user_id)
