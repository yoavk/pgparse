import unittest

import pgparse


class TestCase(unittest.TestCase):
    def test_happy_path(self):
        stmt = 'SELECT * FROM foo ORDER BY bar'
        result = pgparse.deparse_protobuf(pgparse.parse_protobuf(stmt))
        self.assertEqual(result, stmt)
