from abc import ABC, abstractmethod
from typing import List

from gladiator.models.reply import Reply


class GladiatorInterface(ABC):
    @abstractmethod
    def run(self, prompt: str) -> (bool, str, List[Reply]):
        pass
