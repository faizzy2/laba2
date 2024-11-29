import unittest
from reTime import search_time


class TestTime(unittest.TestCase):
    def test_search_time(self):
        self.assertEqual(search_time("23:59:59"), ["23:59:59"])
        self.assertEqual(search_time("24:00:00"), [])
        self.assertEqual(search_time("52:52:52"), [])
        self.assertEqual(search_time("233:32:00"), [])
        self.assertEqual(search_time("12:30:00"), ["12:30:00"])
        self.assertEqual(search_time("00:21:12"), ["00:21:12"])
        self.assertEqual(search_time("00:21:12"), ["00:21:12"])