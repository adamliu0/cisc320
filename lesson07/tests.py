from io import StringIO
import unittest
import lesson07.answer as answer


class Test(unittest.TestCase):
    def no_student(self):
        actual = StringIO('0')
        self.assertEqual(answer.solution(actual),[])

    def one_student(self):
        actual = StringIO('6 \n 1 S 6 2 \n 1 P 1400 3 \n 1 S 8 8 \n 1 T 101 2 \n 1 P 1300 3 \n 1 P 7000 1')
        self.assertEqual(answer.solution(actual), ['1', 1300, 7000, 7])
    
    def one_student_page(self):
        actual = StringIO('1 \n 1 P 1000 3')
        self.assertEqual(answer.solution(actual), [])

    def one_student_submission(self):
        actual = StringIO('1 \n 1 S 9 2')
        self.assertEqual(answer.solution(actual), [])

    def example_test(self):
        actual = StringIO('9 \n 507 P 1000 1 \n 1 S 6 2 \n 1 P 1400 3 \n 1 S 8 8 \n 1 T 101 10 \n 507 S 4 12 \n 1 P 1700 15 \n 1 S 7 16 \n 507 S 8 20')
        self.assertEqual(answer.solution(actual), ['507', 1000, 1000, 6, '1', 1400, 1700, 7])