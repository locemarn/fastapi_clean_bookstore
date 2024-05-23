from abc import ABC, abstractmethod
from typing import List

from src.domain.models.user_model import UserModel


class RepositoryInterface(ABC):
    @abstractmethod
    def get_all(self) -> List[UserModel]: ...

    @abstractmethod
    def insert(self, item: dict) -> UserModel: ...

    @abstractmethod
    def delete(self, id: int) -> UserModel: ...
