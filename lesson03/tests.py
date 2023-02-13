import unittest


class TestLast(unittest.TestCase):
    def test_positive_numbers(self):
        actual = sum(["2\n", "2\n", "3\n"])
        self.assertEqual(actual, "5")

    def test_handles_empty(self):
        actual = sum(["0"])
        self.assertEqual(actual, "EMPTY")

    def test_handles_empty2(self):
        actual = sum([])
        self.assertEqual(actual, "EMPTY")

    def test_negative_numbers(self):
        actual = sum(["4\n", "-3\n", "3\n", "-2\n", "6\n"])
        self.assertEqual(actual, "9")

    def test_999(self):
        actual = sum(["6\n", "4\n", "7\n", "-3\n", "-999\n", "-6\n", "4\n"])
        self.assertEqual(actual, "11")
