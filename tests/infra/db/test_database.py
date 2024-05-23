from faker import Faker
from sqlalchemy import insert

from src.domain.models.user_model import UserModel

fake = Faker()


def test_database(session):
    new_user = UserModel(
        email=fake.email(),
        username=fake.user_name(),
        password=fake.password(),
    )

    sut = session.scalars(
        insert(UserModel).returning(UserModel),
        [
            {
                'email': new_user.email,
                'username': new_user.username,
                'password': new_user.password,
            }
        ],
    ).one()
    assert sut.username == new_user.username
    assert sut.email == new_user.email
    assert sut.password == new_user.password
