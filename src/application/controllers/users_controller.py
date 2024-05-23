from src.application.use_cases.users.delete_user_use_case import (
    DeleteUserUseCase,
)
from src.application.use_cases.users.get_all_users_use_case import (
    GetAllUsersUseCase,
)
from src.application.use_cases.users.insert_user_use_case import (
    InsertUserUseCase,
)
from src.domain.entities.user_entity import UserEntity
from src.domain.models.user_model import UserModel
from src.infra.repositories.user_repository import UserRepository


class UsersController:
    def __init__(self, db_repository: UserRepository):
        self.__db = db_repository

    def get_all_users(self):
        user_entity = UserEntity(self.__db)
        user_use_case = GetAllUsersUseCase(user_entity)
        return user_use_case.execute()

    def insert_new_user(self, user: dict) -> UserModel:
        user_entity = UserEntity(self.__db)
        user_use_case = InsertUserUseCase(user_entity)
        new_user = user_use_case.execute(user)
        return new_user

    def delete_user(self, user_id: int) -> UserModel | Exception:
        user_entity = UserEntity(self.__db)
        user_use_case = DeleteUserUseCase(user_entity)
        deleted_user = user_use_case.execute(user_id)
        return deleted_user
