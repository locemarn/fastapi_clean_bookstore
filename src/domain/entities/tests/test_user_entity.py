import pytest

from src.domain.entities.user_entity import UserEntity


@pytest.fixture()
def user_entity() -> UserEntity:
    return UserEntity(name='test', email='test@email.com', password='secret')


def test_user_entity_exception_name(user_entity: UserEntity):
    with pytest.raises(TypeError) as e:
        user_entity.name = 2
    assert str(e.value) == 'Name must be a string'


def test_user_entity_exception_name_cannot__str_empty(user_entity: UserEntity):
    with pytest.raises(ValueError) as e:
        user_entity.name = ''
    assert str(e.value) == 'Name cannot be empty'


def test_user_entity_exception_name_none(user_entity: UserEntity):
    with pytest.raises(TypeError) as e:
        user_entity.name = {}
    assert str(e.value) == 'Name must be a string'


def test_user_entity_exception_email_not_str(user_entity: UserEntity):
    with pytest.raises(TypeError) as e:
        user_entity.email = 1
    assert str(e.value) == 'Email must be a string'


def test_user_entity_exception_email_cannot_str_empty(user_entity: UserEntity):
    with pytest.raises(ValueError) as e:
        user_entity.email = ''
    assert str(e.value) == 'Email cannot be empty'


def test_user_entity_exception_email():
    with pytest.raises(ValueError, match='Invalid email address') as e:
        UserEntity(name='test', email='test@email', password='secret')
    assert str(e.value) == 'Invalid email address'


def test_user_entity_exception_password_cannot_empty_str(
    user_entity: UserEntity,
):
    with pytest.raises(ValueError, match='Password cannot be empty') as e:
        user_entity.password = ''
    assert str(e.value) == 'Password cannot be empty'


def test_user_entity_exception_password_not_str(user_entity: UserEntity):
    with pytest.raises(TypeError) as e:
        user_entity.password = 1
    assert str(e.value) == 'Password must be a string'


def test_user_entity(user_entity: UserEntity):
    assert user_entity.email == 'test@email.com'
    assert user_entity.password == 'secret'
    assert user_entity.name == 'test'
