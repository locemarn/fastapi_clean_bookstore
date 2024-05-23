from faker import Faker

from src.application.use_cases.users.delete_user_use_case import (
    DeleteUserUseCase,
)
from src.application.use_cases.users.get_all_users_use_case import (
    GetAllUsersUseCase,
)
from src.application.use_cases.users.insert_user_use_case import (
    InsertUserUseCase,
)
from src.domain.entities.user_entity import UserEntity
from src.domain.models.user_model import UserModel

fake = Faker()


def test_users_use_case(in_memory_repository):
    entity = UserEntity(in_memory_repository)
    use_case = GetAllUsersUseCase(entity)
    sut = use_case.execute()
    assert sut == []


def test_insert_new_user(in_memory_repository):
    user = {
        'username': fake.user_name(),
        'email': fake.email(),
        'password': fake.password(),
    }
    entity = UserEntity(in_memory_repository)
    use_case = InsertUserUseCase(entity)
    sut = use_case.execute(user)

    assert isinstance(sut, UserModel)
    assert sut.username == user['username']
    assert sut.email == user['email']
    assert sut.password == user['password']
    assert hasattr(sut, 'id')
    assert hasattr(sut, 'created_at')
    assert hasattr(sut, 'updated_at')


def test_delete_user(in_memory_repository):
    user = {
        'username': fake.user_name(),
        'email': fake.email(),
        'password': fake.password(),
    }
    entity = UserEntity(in_memory_repository)
    use_case = InsertUserUseCase(entity)
    new_user = use_case.execute(user)
    new_user_id = int(new_user.id)

    entity = UserEntity(in_memory_repository)
    use_case = DeleteUserUseCase(entity)
    sut = use_case.execute(new_user_id)

    assert isinstance(sut, UserModel)
    assert sut.id == new_user_id
