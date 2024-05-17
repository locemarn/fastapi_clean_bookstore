from faker import Faker

from src.domain.models.user_model import UserModel

fake = Faker()


def test_user_model():
    email = fake.email()
    username = fake.user_name()
    password = fake.password()
    new_user = UserModel(
        email=email,
        username=username,
        password=password,
    )
    assert isinstance(new_user, UserModel)


def test_user_model_email_validate():
    email = 'as'
    username = fake.user_name()
    password = fake.password()
    user_model = UserModel(
        email=3,
        username=username,
        password=password,
    )

    print('user_model', user_model)


# print('user_model', user_model)
