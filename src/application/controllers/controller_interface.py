from abc import ABC, abstractmethod
from typing import Dict


class ControllerInterface(ABC):
    @abstractmethod
    def handler_insert(self, data: Dict) -> Dict: ...
