import pytest
from faker import Faker
from sqlalchemy import StaticPool, create_engine, delete
from sqlalchemy.orm import Session

from src.domain.models.user_model import UserModel, table_registry
from src.infra.db.database import DatabaseConnection
from src.infra.db.in_memory.in_memory_settings import InMemorySettings
from tests.infra.repositories.in_memory_user_repository import (
    InMemoryUserRepository,
)

fake = Faker()

db = DatabaseConnection()
local_db = db.get_engine()


# @pytest.fixture()
# def client(session):
#     def get_session_override():
#         local = session
#         yield local
#         local.rollback()
#
#     with TestClient(app) as client:
#         app.dependency_overrides[local_db] = get_session_override
#         yield client
#
#     app.dependency_overrides.clear()


@pytest.fixture(scope='session')
def session():
    uri = str(InMemorySettings().DATABASE_URL_TEST)
    engine = create_engine(
        uri,
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        print('session created', session)
        yield session
        session.rollback()

    table_registry.metadata.drop_all(engine)


# @pytest.fixture(scope='session')
# def session():
#     engine = create_engine(
#         InMemorySettings().DATABASE_URL_TEST,
#         connect_args={'check_same_thread': False},
#         poolclass=StaticPool,
#     )
#     session_local = sessionmaker(
#         bind=engine, autoflush=False, autocommit=False
#     )
#     table_registry.metadata.create_all(bind=engine)
#
#     with Session(engine) as session:
#         db_local = session
#         try:
#             yield db_local
#         finally:
#             db_local.close()
#     # yield session()
#     table_registry.metadata.drop_all(bind=engine)


@pytest.fixture(scope='session')
def in_memory_repository(session):
    repo = InMemoryUserRepository(session)
    return repo


@pytest.fixture(autouse=True)
def before_each_user_test(session: Session):
    res = session.execute(delete(UserModel))
    yield res
    session.close()


# @pytest.fixture(scope='session')
# def client(session: Session):
#     with TestClient(app) as client:
#         with DatabaseConnection() as db:
#             # db = DatabaseConnection()
#             app.dependency_overrides[db.get_engine()] = override_test_db
#             yield client
#     app.dependency_overrides.clear()
