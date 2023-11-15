import unittest
from unittest.mock import patch
from PythonFile import calculate_age

class TestCalculateAge(unittest.TestCase):
    
    @patch('builtins.input', return_value='1990-01-01')
    def test_calculate_age(self, mock_input):
        age = calculate_age(mock_input())
        self.assertEqual(age, 33)  # Assuming the test is run in the year 2023

if __name__ == '__main__':
    unittest.main()
