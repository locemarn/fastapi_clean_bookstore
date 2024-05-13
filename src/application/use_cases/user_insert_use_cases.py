import logging
import re
from typing import Dict

from src.application.use_cases.UseCaseInterface import UseCaseInterface
from src.domain.models.user_model import UserModel
from src.domain.repositories.user_repository import UserRepository


class UserInsertUseCase(UseCaseInterface):
    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository

    def execute(self, request: Dict[str, str]) -> Dict[str, str | int]:
        try:
            is_valid_data = self.__validate_data(request)
            if not is_valid_data:
                raise Exception('Invalid data')

            result = self.__register_information(request)
            return self.__format_response(result)
        except Exception as e:
            logging.error('UserInsertUseCase - execute exception')
            logging.error(e)
            raise e

    def __validate_data(self, data: Dict[str, str]) -> bool:
        is_valid_username = self.__validate_username(data['username'])
        is_valid_password = self.__validate_password(data['password'])
        is_valid_email = self.__validate_email(data['email'])

        if not is_valid_username:
            raise Exception('Username already exists')
        if not is_valid_password:
            raise Exception('Invalid password')
        if not is_valid_email:
            raise Exception('Invalid email')
        return True

    @classmethod
    def __validate_username(cls, username: str) -> bool:
        if not username or type(username) is not str:
            raise ValueError('Invalid username')
        return True

    @classmethod
    def __validate_password(cls, password: str) -> bool:
        if not password or type(password) is not str:
            raise ValueError('Invalid password')
        return True

    @classmethod
    def __validate_email(cls, email: str) -> bool:
        if not email or type(email) is not str:
            raise ValueError('Invalid email')
        regex = re.compile(
            r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
        )
        r = re.fullmatch(regex, email)
        return r or True

    def __register_information(self, data: dict[str, str]) -> UserModel:
        return self.__user_repository.insert(data)

    @classmethod
    def __format_response(cls, response: UserModel) -> Dict[str, str | int]:
        return {
            'id': response.id,
            'username': response.username,
            'email': response.email,
            'created_at': response.created_at,
            'updated_at': response.updated_at,
        }
