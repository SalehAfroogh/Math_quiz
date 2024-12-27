import unittest
from unittest.mock import patch
import io
import time
import random

class TestMathQuiz(unittest.TestCase):
    def setUp(self):
        self.start_time = time.time()

    @patch('builtins.input', side_effect=['2', '0', '9', '8', '0'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_correct_answers(self, mock_stdout, mock_input):
        """Test scenario where all answers are correct and within time limit."""
        with patch('random.randint', side_effect=[1, 1, 2, 2, 3, 3, 4, 4, 5, 5]):
            with patch('random.choice', side_effect=['+', '-', '*', '+', '-']):
                with open("math_quiz.py") as f:
                    exec(f.read())

        output = mock_stdout.getvalue()
        self.assertIn("Perfect! Your score is 5", output)
        self.assertIn("Final score is 5 out of 5", output)

    @patch('builtins.input', side_effect=['1', '0', '3', '5', '6'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_incorrect_answers(self, mock_stdout, mock_input):
        """Test scenario where some answers are incorrect."""
        with patch('random.randint', side_effect=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]):
            with patch('random.choice', side_effect=['+', '-', '*', '+', '-']):
                with open("math_quiz.py") as f:
                    exec(f.read())

        output = mock_stdout.getvalue()
        self.assertIn("Sorry, it is wrong.", output)
        self.assertIn("Final score is", output)

    @patch('builtins.input', side_effect=['0', '0', '0', '0', '0'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_exceed_time_limit(self, mock_stdout, mock_input):
        """Test scenario where user exceeds time limit for each question."""
        with patch('random.randint', side_effect=[1, 1, 2, 2, 3, 3, 4, 4, 5, 5]):
            with patch('random.choice', side_effect=['+', '-', '*', '+', '-']):
                with patch('time.time', side_effect=[self.start_time, self.start_time + 6] * 5):
                    with open("math_quiz.py") as f:
                        exec(f.read())

        output = mock_stdout.getvalue()
        self.assertIn("You are too late!", output)
        self.assertIn("Final score is 0 out of 5", output)

if __name__ == '__main__':
    unittest.main()
