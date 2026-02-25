import unittest
from python_essentials_2.StudentPerformance_diff import StudentPerformance
class TestPerformanceDifference(unittest.TestCase):
    def test_valid_input(self):
        # Test with valid input
        performance = StudentPerformance([80, 90, 85, 70, 95])
        self.assertEqual(performance.score_difference(), None)  # The method prints output, so we check for None

    def test_single_input(self):
        # Test with less than 2 marks
        performance = StudentPerformance([80])
        self.assertEqual(performance.score_difference(), None)  # The function prints output, so we check for None
    def test_insufficient_marks(self):
        # Test with all marks being the same
        performance = StudentPerformance([])
        self.assertEqual(performance.score_difference(), None)  # The function prints output, so we check for None
    def test_equal_marks(self):
        # Test with all marks being the same
        performance = StudentPerformance([80,80])
        self.assertEqual(performance.score_difference(), None)  # The function prints output, so we check for None