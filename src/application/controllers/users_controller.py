from sqlalchemy.orm import Session

from src.application.use_cases.user_insert_use_cases import UsersUseCases


class UsersController:
    def __init__(self, db: Session):
        self.db = db

    def insert_user(self, user: dict):
        if not user['username']:
            raise ValueError('Username cannot be empty')

        if (
            type(user['username'])
            or type(user['email'])
            or type(user['username'])
        ) is not str:
            raise ValueError('Data must be a string')

        user_use_case = UsersUseCases()
        response = user_use_case.insert(
            user=user,
        )
        return response
