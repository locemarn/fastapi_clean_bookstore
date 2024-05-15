import pytest
from faker import Faker
from sqlalchemy.orm import Session

from src.domain.repositories.user_repository import UserRepository

fake = Faker()


def test_user_repository_exception_email(session: Session):
    data: dict[str, str] = {
        'email': None,
        'username': fake.user_name(),
        'password': fake.password(),
    }
    user_repository = UserRepository()

    with pytest.raises(TypeError, match='Email must be a string') as e:
        user_repository.insert(data)

    assert str(e.value) == 'Email must be a string'


def test_user_repository_exception_password(session: Session):
    data: dict[str, str] = {
        'email': fake.email(),
        'username': fake.user_name(),
        'password': None,
    }
    user_repository = UserRepository()

    with pytest.raises(TypeError, match='Password must be a string') as e:
        user_repository.insert(data)

    assert str(e.value) == 'Password must be a string'


def test_user_repository_exception_username(session: Session):
    data: dict[str, str] = {
        'email': fake.email(),
        'username': None,
        'password': fake.password(),
    }
    user_repository = UserRepository()

    with pytest.raises(TypeError, match='Username must be a string') as e:
        user_repository.insert(data)

    assert str(e.value) == 'Username must be a string'


def test_user_repository(session: Session):
    data: dict[str, str] = {
        'email': fake.email(),
        'username': fake.user_name(),
        'password': fake.password(),
    }
    user_repository = UserRepository()
    sut = user_repository.insert(data)

    assert sut.email == data['email']
    assert sut.username == data['username']
    assert sut.password == data['password']

    assert hasattr(sut, 'id')
    assert hasattr(sut, 'created_at')
    assert hasattr(sut, 'updated_at')
