from sqlalchemy.orm import Session

from tests.infra.repositories.in_memory_user_repository import (
    InMemoryUserRepository,
)


def test_user_repository(session: Session):
    sut = InMemoryUserRepository(session)
    assert isinstance(sut, InMemoryUserRepository)
