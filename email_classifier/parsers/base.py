from email.message import EmailMessage
from typing import Optional
from abc import ABC, abstractmethod

from ..structs import AccurateParse


class Parser(ABC):
    @abstractmethod
    def try_parse(self, email: EmailMessage) -> Optional[AccurateParse]:
        pass
