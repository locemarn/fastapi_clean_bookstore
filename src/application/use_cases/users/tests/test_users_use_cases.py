from faker import Faker
from sqlalchemy.orm import Session

from src.application.use_cases.users.users_use_cases import UsersUseCases
from src.domain.entities.user_entity import UserEntity
from src.domain.models.user_model import UserModel

fake = Faker()


def test_users_use_case_insert(session: Session) -> None:
    new_user = UserEntity(
        username=fake.name(), email=fake.email(), password=fake.pystr()
    )

    users_use_case = UsersUseCases()

    sut = users_use_case.insert(session, new_user)

    assert isinstance(sut['user'], UserModel)
