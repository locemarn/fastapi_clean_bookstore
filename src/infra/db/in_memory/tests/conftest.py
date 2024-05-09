import pytest
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import Session, sessionmaker

from src.domain.models.user_model import Base
from src.infra.db.in_memory.in_memory_settings import InMemorySettings

engine = create_engine(InMemorySettings().DATABASE_URL_TEST)


@pytest.fixture(scope='session')
def session():
    engine = create_engine(
        InMemorySettings().DATABASE_URL_TEST,
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    yield Session()
    Base.metadata.drop_all(engine)


def get_session():
    with Session(bind=engine) as session:
        yield session
