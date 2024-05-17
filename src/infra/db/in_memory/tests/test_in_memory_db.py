from faker import Faker
from sqlalchemy import select

from src.domain.models.user_model import UserModel

fake = Faker()


def test_create(session):
    email = fake.email()
    username = fake.user_name()
    password = fake.password()
    new_user = UserModel(
        email=email,
        username=username,
        password=password,
    )
    session.add(new_user)
    session.commit()

    user = session.scalar(
        select(UserModel).where(UserModel.username == username)
    )
    assert user.username == username
