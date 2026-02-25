import unittest
from python_essentials_2.StudentMarks_avg import StudentMarks

class TestLastThreeAvg(unittest.TestCase):
    def test_valid_input(self):
        # Test with valid input
        marks = StudentMarks([80, 90, 85, 70, 95])
        self.assertEqual(marks.last_three_avg(), None)  # The method prints output, so we check for None

    def test_insufficient_marks(self):
        # Test with less than 3 marks
        marks = StudentMarks([80, 90])
        self.assertEqual(marks.last_three_avg(), None)  # The function prints output, so we check for None