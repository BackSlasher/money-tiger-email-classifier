from typing import Optional
from email.message import EmailMessage
from .structs import AccurateParse
from .parsers.wolt import WoltParser


def collect_parsers():
    return [
        WoltParser(),
    ]


class Factory:
    def __init__(self):
        self.parsers = collect_parsers()

    def parse(self, email: EmailMessage) -> Optional[AccurateParse]:
        for parser in self.parsers:
            try:
                res = parser.try_parse(email)
            except:
                # TODO log
                res = None
            if res:
                return res
        return None
