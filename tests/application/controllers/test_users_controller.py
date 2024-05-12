# import pytest
# from faker import Faker
# from sqlalchemy.orm import Session
#
# from src.application.controllers.users_controller import UsersController
# from src.domain.models.user_model import UserModel
#
# fake = Faker()
#
#
# def test_users_controller_with_none_username(session: Session):
#     new_user = {
#         'username': None,
#         'email': fake.email(),
#         'password': fake.password(),
#     }
#     user_controller = UsersController(session)
#     with pytest.raises(ValueError, match='Username cannot be empty') as e:
#         user_controller.insert_user(user=new_user)
#     assert str(e.value) == 'Username cannot be empty'
#
#
# def test_users_controller_with_not_str_username(session: Session):
#     new_user = {
#         'username': 1,
#         'email': fake.email(),
#         'password': fake.password(),
#     }
#     user_controller = UsersController(session)
#     with pytest.raises(ValueError, match='Data must be a string') as e:
#         user_controller.insert_user(user=new_user)
#     assert str(e.value) == 'Data must be a string'
#
#
# def test_users_controller(session: Session):
#     new_user = {
#         'username': fake.user_name(),
#         'email': fake.email(),
#         'password': fake.password(),
#     }
#     user_controller = UsersController(session)
#     sut = user_controller.insert_user(new_user)
#     assert isinstance(sut['user'], UserModel)
