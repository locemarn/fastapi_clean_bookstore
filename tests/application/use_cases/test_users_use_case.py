import pytest
from faker import Faker

from src.application.use_cases.user_insert_use_cases import UserInsertUseCase
from src.domain.models.user_model import UserModel

fake = Faker()


class UserRepositorySpy:
    def __init__(self):
        self.insert_user_attributes = {}
        self.select_user_attributes = {}

    def insert(self, attributes: dict) -> UserModel:
        self.insert_user_attributes['email'] = attributes['email']
        self.insert_user_attributes['username'] = attributes['username']
        self.insert_user_attributes['password'] = attributes['password']
        return self.select_user(self.insert_user_attributes)

    def select_user(self, attributes: dict) -> UserModel:
        # self.select_user_attributes['username'] = attributes['username']
        return UserModel(**attributes)


def test_users_use_case_username_error(new_user_dict):
    print('new_user_dict', new_user_dict)

    repo = UserRepositorySpy()
    username = new_user_dict['username']
    new_user_dict['username'] = 3
    repo.select_user(new_user_dict)
    user_user_case = UserInsertUseCase(repo)

    with pytest.raises(ValueError, match='Invalid username') as e:
        user_user_case.execute(new_user_dict)
    assert str(e.value) == 'Invalid username'
    new_user_dict['username'] = username


def test_users_use_case_password_error(new_user_dict):
    repo = UserRepositorySpy()
    password = new_user_dict['password']
    new_user_dict['password'] = 3
    repo.select_user(new_user_dict)
    user_user_case = UserInsertUseCase(repo)
    with pytest.raises(ValueError, match='Invalid password') as e:
        user_user_case.execute(new_user_dict)
    print(e.value)
    assert str(e.value) == 'Invalid password'
    new_user_dict['password'] = password


def test_users_use_case_mail_error(new_user_dict):
    repo = UserRepositorySpy()
    email = new_user_dict['email']
    new_user_dict['email'] = 3
    repo.select_user(new_user_dict)
    user_user_case = UserInsertUseCase(repo)
    with pytest.raises(ValueError, match='Invalid email') as e:
        user_user_case.execute(new_user_dict)
    assert str(e.value) == 'Invalid email'
    new_user_dict['email'] = email


def test_users_use_case(new_user_dict):
    repo = UserRepositorySpy()
    repo.select_user(new_user_dict)
    user_user_case = UserInsertUseCase(repo)
    sut = user_user_case.execute(new_user_dict)

    assert sut['email'] == new_user_dict['email']
    assert sut['username'] == new_user_dict['username']
