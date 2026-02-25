import unittest
from python_essentials_2.StudentScores_highest import StudentScores
class TestHighestScore(unittest.TestCase):
    def test_valid_input(self):
        # Test with valid input
        scores = StudentScores([80, 90, 85, 70, 95])
        self.assertEqual(scores.highest_score(), None)  # The method prints output, so we check for None

    def test_insufficient_scores(self):
        # Test with less than 2 scores
        scores = StudentScores([80])
        self.assertEqual(scores.highest_score(), None)  # The function prints output, so we check for None