from abc import ABC, abstractmethod


class RepositoryInterface(ABC):
    @abstractmethod
    def insert(self):
        pass
