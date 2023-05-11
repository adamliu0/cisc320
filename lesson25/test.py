import unittest
from answer import tsp


class TestTSP(unittest.TestCase):
    def test_tsp(self):
        # Test case 1
        adj_matrix = [
            [0, 2, 9, 10],
            [1, 0, 6, 4],
            [15, 7, 0, 8],
            [6, 3, 12, 0]
        ]
        start_node = 0
        expected_path = [0, 1, 3, 2, 0]
        expected_dist = 33
        path, dist = tsp(adj_matrix, start_node)
        self.assertEqual(path, expected_path)
        self.assertEqual(dist, expected_dist)

        # Test case 2
        adj_matrix = [
            [0, 3, 1],
            [2, 0, 4],
            [3, 1, 0]
        ]
        start_node = 2
        expected_path = [2, 1, 0, 2]
        expected_dist = 4
        path, dist = tsp(adj_matrix, start_node)
        self.assertEqual(path, expected_path)
        self.assertEqual(dist, expected_dist)


class Test_example(unittest.TestCase):
    def test_example(self):
        adj_matrix = [
            [0, 29, 82, 46, 68, 52, 72, 42, 51, 55, 29, 74, 23, 72, 46],
            [29, 0, 55, 46, 42, 43, 43, 23, 23, 31, 41, 51, 11, 52, 21],
            [82, 55, 0, 68, 46, 55, 23, 43, 41, 29, 79, 21, 64, 31, 51],
            [46, 46, 68, 0, 82, 15, 72, 31, 62, 42, 21, 51, 51, 43, 64],
            [68, 42, 46, 82, 0, 74, 23, 52, 21, 46, 82, 58, 46, 65, 23],
            [52, 43, 55, 15, 74, 0, 61, 23, 55, 31, 33, 37, 51, 29, 59],
            [72, 43, 23, 72, 23, 61, 0, 42, 23, 31, 77, 37, 51, 46, 33],
            [42, 23, 43, 31, 52, 23, 42, 0, 33, 15, 37, 33, 33, 31, 37],
            [51, 23, 41, 62, 21, 55, 23, 33, 0, 29, 62, 46, 29, 51, 11],
            [55, 31, 29, 42, 46, 31, 31, 15, 29, 0, 51, 21, 41, 23, 37],
            [29, 41, 79, 21, 82, 33, 77, 37, 62, 51, 0, 65, 42, 59, 61],
            [74, 51, 21, 51, 58, 37, 37, 33, 46, 21, 65, 0, 61, 11, 55],
            [23, 11, 64, 51, 46, 51, 51, 33, 29, 41, 42, 61, 0, 62, 23],
            [72, 52, 31, 43, 65, 29, 46, 31, 51, 23, 59, 11, 62, 0, 59],
            [46, 21, 51, 64, 23, 59, 33, 37, 11, 37, 61, 55, 23, 59, 0]
        ]
        start_node = 5
        expected_path = [5, 3, 10, 0, 12, 1, 14, 8, 4, 6, 2, 11, 13, 9, 7, 5]
        expected_dist = 291
        path, dist = tsp(adj_matrix, start_node)
        self.assertEqual(path, expected_path)
        self.assertEqual(dist, expected_dist)

if __name__ == '__main__':
    unittest.main()
