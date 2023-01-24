from typing import NamedTuple
from decimal import Decimal
import datetime


class Payment(NamedTuple):
    currency: str
    amount: Decimal


class AccurateParse(NamedTuple):
    company: str
    account: str
    payment: Payment
    time: datetime.time
