from abc import ABC, abstractmethod

from sqlalchemy.orm import Session


class RepositoryInterface(ABC):
    @abstractmethod
    def insert(self, db: Session):
        pass
