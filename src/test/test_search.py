from deepdiff import DeepDiff  # type: ignore

from unittest import TestCase

from util import Address
from search import query_db


class TestSearch(TestCase):
    def test_query_db(self):
        tests = [
            "abaigar 4, navarra",
            "calle josé maría 2, Pamplona",
            "unexisting"
        ]
        actuals = [query_db(t) for t in tests]
        expected = [
            Address(**{
                "lon": -2.1414442,
                "lat": 42.6489724,
                "number": 4,
                "street": "CALLE CALLEJA",
                "city": "Abáigar",
                "district": "Abáigar",
                "region": "Navarra",
                "postcode": "31280",
            }),
            Address(**{
                "lon": -1.6398572,
                "lat": 42.8015041,
                "number": "2 181",
                "street": "CALLE JOSE MARIA JIMENO JURIO",
                "unit": None,
                "city": "Pamplona / Iruña",
                "district": "Pamplona / Iruña",
                "region": "Navarra",
                "postcode": 31006,
                "id": 125632,
                "hash": "7f72a12503865d51",
            }),
            None
        ]
        self.assertEqual(
            DeepDiff(expected, actuals, ignore_order=True),
            {},
        )
