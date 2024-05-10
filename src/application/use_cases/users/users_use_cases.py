from sqlalchemy.orm import Session

from src.domain.entities.user_entity import UserEntity
from src.domain.repositories.repository_interface import RepositoryInterface


class UsersUseCases:
    def __init__(self, repository: RepositoryInterface = RepositoryInterface):
        self._repo = repository

    @classmethod
    def insert(cls, db: Session, user: UserEntity):
        user_entity = UserEntity(
            username=user.username,
            email=user.email,
            password=user.password,
        )
        return user_entity.insert(db)
