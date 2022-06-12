import unittest

import pgparse


class TestCase(unittest.TestCase):
    def test_happy_path(self):
        stmt = 'SELECT * FROM foo ORDER BY bar'
        result = pgparse.protobuf_deparse(pgparse.protobuf_parse(stmt))
        self.assertEqual(result, stmt)
