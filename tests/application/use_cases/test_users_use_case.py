import pytest
from faker import Faker

from src.application.use_cases.user_insert_use_cases import UserInsertUseCase
from src.domain.models.user_model import UserModel

fake = Faker()


class UserRepositorySpy:
    def __init__(self) -> any:
        self.insert_user_attributes = {}
        self.select_user_attributes = {}

    def insert(self, attributes: dict) -> UserModel:
        self.insert_user_attributes['email'] = attributes['email']
        self.insert_user_attributes['username'] = attributes['username']
        self.insert_user_attributes['password'] = attributes['password']
        return self.select_user(self.insert_user_attributes)

    def select_user(self, attributes: dict) -> UserModel:
        self.select_user_attributes['username'] = attributes['username']
        return UserModel(**attributes)


def test_users_use_case_username_error():
    data: dict[str, str] = {
        'email': str(fake.email()),
        'username': str(fake.user_name()),
        'password': str(fake.password()),
    }
    repo = UserRepositorySpy()
    data['username'] = 3
    repo.select_user(data)
    user_user_case = UserInsertUseCase(repo)

    with pytest.raises(ValueError, match='Invalid username') as e:
        user_user_case.execute(data)
    assert str(e.value) == 'Invalid username'


def test_users_use_case_password_error():
    data: dict[str, str] = {
        'email': str(fake.email()),
        'username': str(fake.user_name()),
        'password': str(fake.password()),
    }
    repo = UserRepositorySpy()
    data['password'] = 3
    repo.select_user(data)
    user_user_case = UserInsertUseCase(repo)
    with pytest.raises(ValueError, match='Invalid password') as e:
        user_user_case.execute(data)
    assert str(e.value) == 'Invalid password'


def test_users_use_case_mail_error():
    data: dict[str, str] = {
        'email': str(fake.email()),
        'username': str(fake.user_name()),
        'password': str(fake.password()),
    }
    repo = UserRepositorySpy()
    data['email'] = 3
    repo.select_user(data)
    user_user_case = UserInsertUseCase(repo)
    with pytest.raises(ValueError, match='Invalid email') as e:
        user_user_case.execute(data)
    assert str(e.value) == 'Invalid email'


def test_users_use_case():
    data: dict[str, str] = {
        'email': str(fake.email()),
        'username': str(fake.user_name()),
        'password': str(fake.password()),
    }
    repo = UserRepositorySpy()
    repo.select_user(data)
    user_user_case = UserInsertUseCase(repo)
    sut = user_user_case.execute(data)

    assert sut['email'] == data['email']
    assert sut['password'] == data['password']
    assert sut['username'] == data['username']
