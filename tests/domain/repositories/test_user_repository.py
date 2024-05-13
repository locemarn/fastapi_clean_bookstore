from faker import Faker
from sqlalchemy.orm import Session

from src.domain.repositories.user_repository import UserRepository

fake = Faker()


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
