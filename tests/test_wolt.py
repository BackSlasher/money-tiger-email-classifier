from unittest import TestCase
import email
import email.policy
from decimal import Decimal
import datetime

from email_classifier import structs
from email_classifier.parser_factory import Factory
from email_classifier.parsers import wolt


class WoltTest(TestCase):
    def test_main(self):
        with open("tests/inputs/wolt.email", "rb") as f:
            buffer = f.read()
        e = email.message_from_bytes(buffer, policy=email.policy.default)
        parser = wolt.WoltParser()
        res = parser.try_parse(e)
        expected = structs.AccurateParse(
            company="wolt",
            account="1234",
            payment=structs.Payment(currency="ILS", amount=Decimal("137.00")),
            time=datetime.datetime(2023, 1, 21, 16, 40),
        )
        self.assertEqual(res, expected)

    def test_factory(self):
        with open("tests/inputs/wolt.email", "rb") as f:
            buffer = f.read()
        e = email.message_from_bytes(buffer, policy=email.policy.default)
        factory = Factory()
        res = factory.parse(e)
        expected = structs.AccurateParse(
            company="wolt",
            account="1234",
            payment=structs.Payment(currency="ILS", amount=Decimal("137.00")),
            time=datetime.datetime(2023, 1, 21, 16, 40),
        )
        self.assertEqual(res, expected)
