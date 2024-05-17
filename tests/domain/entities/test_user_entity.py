# import pytest
#
# from src.domain.models.user_model import UserModel
#
#
# # from src.domain.entities.user_entity import UserEntity
#
#
# def test_user_entity_exception_username(user_entity: UserModel):
#     with pytest.raises(TypeError) as e:
#         user_entity.username = 2
#     assert str(e.value) == 'username must be a string'
#
#
# def test_user_entity_exception_username_cannot__str_empty(
#     user_entity: UserModel,
# ):
#     with pytest.raises(ValueError, match='username cannot be empty') as e:
#         user_entity.username = ''
#     assert str(e.value) == 'username cannot be empty'
#
#
# def test_user_entity_exception_username_none(user_entity: UserModel):
#     with pytest.raises(TypeError) as e:
#         user_entity.username = {}
#     assert str(e.value) == 'username must be a string'
#
#
# def test_user_entity_exception_email_not_str(user_entity: UserModel):
#     with pytest.raises(TypeError) as e:
#         user_entity.email = 1
#     assert str(e.value) == 'Email must be a string'
#
#
# def test_user_entity_exception_email_cannot_str_empty(user_entity: UserModel):
#     with pytest.raises(ValueError, match='Email cannot be empty') as e:
#         user_entity.email = ''
#     assert str(e.value) == 'Email cannot be empty'
#
#
# def test_user_entity_exception_email():
#     with pytest.raises(ValueError, match='Invalid email address') as e:
#         UserEntity(username='test', email='test@email', password='secret')
#     assert str(e.value) == 'Invalid email address'
#
#
# def test_user_entity_exception_password_cannot_empty_str(
#     user_entity: UserEntity,
# ):
#     with pytest.raises(ValueError, match='Password cannot be empty') as e:
#         user_entity.password = ''
#     assert str(e.value) == 'Password cannot be empty'
#
#
# def test_user_entity_exception_password_not_str(user_entity: UserEntity):
#     with pytest.raises(TypeError) as e:
#         user_entity.password = 1
#     assert str(e.value) == 'Password must be a string'
#
#
# def test_user_entity(user_entity: UserEntity):
#     assert isinstance(user_entity, UserEntity)
#     assert hasattr(user_entity, 'email')
#     assert hasattr(user_entity, 'password')
#     assert hasattr(user_entity, 'username')
