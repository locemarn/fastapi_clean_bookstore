import pytest
from faker import Faker
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import sessionmaker
from starlette.testclient import TestClient

from app import app
from src.domain.entities.user_entity import UserEntity
from src.domain.models.user_model import Base, UserModel
from src.infra.db.in_memory.in_memory_settings import InMemorySettings

fake = Faker()


@pytest.fixture(scope='session')
def session():
    engine = create_engine(
        InMemorySettings().DATABASE_URL_TEST,
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )
    session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    yield session()
    Base.metadata.drop_all(engine)


@pytest.fixture(scope='session')
def client(session):
    def get_session_override():
        return session

    with TestClient(app) as client:
        yield client


@pytest.fixture()
def user_entity() -> UserEntity:
    return UserEntity(
        username=fake.user_name(),
        email=fake.email(),
        password=fake.password(),
    )


@pytest.fixture(scope='session')
def new_user_model() -> UserModel:
    email = fake.email()
    username = fake.user_name()
    password = fake.password()
    new_user = UserModel(
        email=email,
        username=username,
        password=password,
    )
    return new_user


@pytest.fixture(scope='session')
def new_user_dict() -> dict[str, str]:
    data = {
        'email': str(fake.email()),
        'username': str(fake.user_name()),
        'password': str(fake.password()),
    }
    return data


@pytest.fixture(scope='session', autouse=True)
def create_user_dict(new_user_dict) -> dict[str, str]:
    print('fixture new_user_dict ---->', new_user_dict)
    new_user_dict = {
        'email': str(fake.email()),
        'username': str(fake.user_name()),
        'password': str(fake.password()),
    }
    return new_user_dict


@pytest.fixture(scope='session')
def reset_new_user_dict() -> dict[str, str]:
    data: dict[str, str] = {
        'email': str(fake.email()),
        'username': str(fake.user_name()),
        'password': str(fake.password()),
    }
    return data
