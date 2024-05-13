from abc import ABC, abstractmethod
from typing import Dict


class UseCaseInterface(ABC):
    @abstractmethod
    def execute(self, request: Dict) -> Dict: ...
