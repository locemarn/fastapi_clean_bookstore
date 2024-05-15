from abc import ABC, abstractmethod


class RepositoryInterface(ABC):
    @abstractmethod
    def insert(self, data: dict[str, str]) -> None:
        pass
