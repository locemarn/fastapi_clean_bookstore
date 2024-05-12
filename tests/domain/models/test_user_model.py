from faker import Faker

from src.domain.models.user_model import UserModel

fake = Faker()


def test_user_model():
    user_model = UserModel(
        email=fake.email(),
        username=fake.user_name(),
        password=fake.password(),
    )
    assert isinstance(user_model, UserModel)
