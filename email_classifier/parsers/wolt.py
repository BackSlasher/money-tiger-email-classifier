import re
import datetime
from typing import Optional
from bs4 import BeautifulSoup
from decimal import Decimal

from ..parsers.base import Parser
from ..structs import AccurateParse, Payment
from email.message import EmailMessage


class WoltParser(Parser):
    def try_parse(self, email: EmailMessage) -> Optional[AccurateParse]:
        payload = email.get_body().get_payload(decode=True)
        # Assuming this is html
        soup = BeautifulSoup(payload, "html.parser")
        (link,) = soup.select("div.gmail_attr > span > a")
        frommail = link.text
        assert frommail == "info@wolt.com"
        # Find sum
        cc_bill_re = re.compile(r"\*+(\d{4})$")
        (cc_element,) = soup(string=cc_bill_re)
        cc = cc_bill_re.search(cc_element.text).group(1)
        total_element = cc_element.find_next()
        total_text = total_element.text
        total_text = total_text.replace("\u200e", "")
        total = Decimal(total_text)
        (time_title_element,) = soup(string="תאריך הפקה")
        time_element = time_title_element.find_next()
        time_text = time_element.text
        time = datetime.datetime.strptime(time_text, "%d.%m.%Y %H:%M")

        return AccurateParse(
            company="wolt",
            payment=Payment(currency="ILS", amount=total),
            account=cc,
            time=time,
        )
