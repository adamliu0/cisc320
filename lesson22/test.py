import unittest
import answer

class Test_get_list_of_items(unittest.TestCase):
    def test_get_list_of_items(self):
        lines = ["apple 10 5", "banana 6 4", "carrot 3 2"]
        expected = [
            {"name": "apple", "weight": 10, "value": 5},
            {"name": "banana", "weight": 6, "value": 4},
            {"name": "carrot", "weight": 3, "value": 2}
        ]
        self.assertEqual(answer.get_list_of_items(lines), expected)
    
    def test_get_list_given(self):
        lines = [
            "Textbook 4 50\n",
            "HardDrive 10 2\n",
            "DogFood 10 5\n",
            "FavoriteGame 20 60\n",
            "SuperComputer 100 100\n",
        ]
        expected = [
            {"name": "Textbook", "weight": 4, "value": 50},
            {"name": "HardDrive", "weight": 10, "value": 2},
            {"name": "DogFood", "weight": 10, "value": 5},
            {"name": "FavoriteGame", "weight": 20, "value": 60},
            {"name": "SuperComputer", "weight": 100, "value": 100},
        ]
        self.assertEqual(answer.get_list_of_items(lines), expected)

class Test_table(unittest.TestCase):
    def test_table(self):
        items = [
            {"name": "apple", "weight": 10, "value": 5},
            {"name": "banana", "weight": 6, "value": 4},
            {"name": "carrot", "weight": 3, "value": 2}
        ]
        capacity = 10
        expected = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
            [0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 5],
            [0, 0, 0, 2, 2, 2, 4, 4, 6, 6, 6],
            [0, 0, 0, 2, 2, 2, 4, 4, 6, 6, 7]
        ]
        self.assertEqual(answer.table(items, capacity), expected)

class Test_get_items(unittest.TestCase):
    def test_get_items(self):
        table = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
            [0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 5],
            [0, 0, 0, 2, 2, 2, 4, 4, 6, 6, 6],
            [0, 0, 0, 2, 2, 2, 4, 4, 6, 6, 7]
        ]
        expected = [
            {"name": "banana", "weight": 6, "value": 4},
            {"name": "carrot", "weight": 3, "value": 2}
        ]
        self.assertEqual(answer.get_items(table), expected)