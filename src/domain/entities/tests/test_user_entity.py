import pytest
from sqlalchemy.orm import Session

from src.domain.entities.user_entity import UserEntity


@pytest.fixture()
def user_entity() -> UserEntity:
    return UserEntity(
        username='test', email='test@email.com', password='secret'
    )


def test_user_entity_exception_username(user_entity: UserEntity):
    with pytest.raises(TypeError) as e:
        user_entity.username = 2
    assert str(e.value) == 'username must be a string'


def test_user_entity_exception_username_cannot__str_empty(
    user_entity: UserEntity,
):
    with pytest.raises(ValueError, match='username cannot be empty') as e:
        user_entity.username = ''
    assert str(e.value) == 'username cannot be empty'


def test_user_entity_exception_username_none(user_entity: UserEntity):
    with pytest.raises(TypeError) as e:
        user_entity.username = {}
    assert str(e.value) == 'username must be a string'


def test_user_entity_exception_email_not_str(user_entity: UserEntity):
    with pytest.raises(TypeError) as e:
        user_entity.email = 1
    assert str(e.value) == 'Email must be a string'


def test_user_entity_exception_email_cannot_str_empty(user_entity: UserEntity):
    with pytest.raises(ValueError, match='Email cannot be empty') as e:
        user_entity.email = ''
    assert str(e.value) == 'Email cannot be empty'


def test_user_entity_exception_email():
    with pytest.raises(ValueError, match='Invalid email address') as e:
        UserEntity(username='test', email='test@email', password='secret')
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
    assert user_entity.username == 'test'


def test_user_entity_insert_user_exception(
    user_entity: UserEntity, session: Session
):
    session = None
    with pytest.raises(
        Exception, match="'NoneType' object has no attribute 'rollback'"
    ) as e:
        user_entity.insert(session)
    assert str(e.value) == "'NoneType' object has no attribute 'rollback'"


def test_user_entity_insert_user_exception_if_user_already_exist(
    user_entity: UserEntity, session: Session
):
    user_entity.insert(session)
    with pytest.raises(
        ValueError, match=f'User {user_entity.email} already exists'
    ) as e:
        user_entity.insert(session)
    assert str(e.value) == f'User {user_entity.email} already exists'


def test_user_entity_insert_user(user_entity: UserEntity, session: Session):
    user = user_entity.insert(session)
    assert user['user'].username == user_entity.username
    assert user['user'].email == user_entity.email
    assert user['user'].password == user_entity.password
