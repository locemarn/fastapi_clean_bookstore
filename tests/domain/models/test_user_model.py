from faker import Faker

from src.domain.models.user_model import UserModel

fake = Faker()


def test_user_model(new_user_model):
    assert isinstance(new_user_model, UserModel)


# def test_user_model_email_validate():
#     email = fake.email()
#     username = 3
#     password = fake.password()
#     user_model = UserModel(
#         email=email,
#         username=username,
#         password=password,
#     )

# print('user_model', user_model.validate_email('email', 'test@email.com'))
# print('user_model', user_model)
