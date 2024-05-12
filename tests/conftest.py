# import pytest
# from sqlalchemy import StaticPool, create_engine
# from sqlalchemy.orm import sessionmaker
#
# from src.domain.entities.user_entity import UserEntity
# from src.domain.models.user_model import Base
# from src.infra.db.in_memory.in_memory_settings import InMemorySettings
#
# # @pytest.fixture(scope='session')
# # def client(session):
# #     def get_session_override():
# #         return session
# #
# #     with TestClient(app) as client:
# #         app.dependency_override[get_session] = get_session_override
# #         yield client
# #     app.dependency_override.clear()
#
#
import pytest
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import sessionmaker

from src.domain.models.user_model import Base
from src.infra.db.in_memory.in_memory_settings import InMemorySettings


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


#
#
# @pytest.fixture()
# def user_entity() -> UserEntity:
#     return UserEntity(
#         username='test', email='test@email.com', password='secret'
#     )