from faker import Faker

from src.application.controllers.users_controller import UsersController
from src.domain.models.user_model import UserModel

fake = Faker()


def test_users_controller_get_all(in_memory_repository, session):
    controller = UsersController(in_memory_repository)
    sut = controller.get_all_users()
    assert sut == []


def test_users_controller_insert(in_memory_repository, session):
    user = {
        'username': fake.user_name(),
        'email': fake.email(),
        'password': fake.password(),
    }

    controller = UsersController(in_memory_repository)
    sut = controller.insert_new_user(user)

    assert isinstance(sut, UserModel)
    assert sut.username == user['username']
    assert sut.email == user['email']
    assert sut.password == user['password']
    assert hasattr(sut, 'id')
    assert hasattr(sut, 'created_at')
    assert hasattr(sut, 'updated_at')


def test_users_controller_delete(in_memory_repository):
    user = {
        'username': fake.user_name(),
        'email': fake.email(),
        'password': fake.password(),
    }
    controller = UsersController(in_memory_repository)
    new_user = controller.insert_new_user(user)
    user_id = int(new_user.id)

    sut = controller.delete_user(user_id)

    assert isinstance(sut, UserModel)
    assert sut.id == user_id


def test_users_controller_delete_exception_with_id_not_int(
    in_memory_repository,
):
    controller = UsersController(in_memory_repository)
    sut = controller.delete_user(None)
    assert sut is None
