# from typing import Annotated
#
# from fastapi import Depends
# from sqlalchemy import select
# from sqlalchemy.orm import Session
#
# from src.domain.entities.user_entity import UserEntity
# from src.domain.models.user_model import UserModel
# from src.domain.repositories.repository_interface import RepositoryInterface
# from src.infra.db.in_memory.tests.conftest import session
#
# Session = Annotated[Session, Depends(session)]
#
#
# class UsersInMemoryRepository(RepositoryInterface):
#     def __init__(self, db: Session) -> None:
#         self.db = db
#
#     def insert(self, user: UserEntity) -> UserModel:
#         # new_user = UserEntity(
#         #     username='test',
#         #     email='test@email.com',
#         #     password='secret',
#         # )
#         u = self.db.scalars(select(UserModel))
#         print('uuuu', u)
#         return u
