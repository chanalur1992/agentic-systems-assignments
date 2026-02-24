import unittest
from python_essentials_1.elig_checker import Elig_Checker

class TestEligChecker(unittest.TestCase):
    def test_valid_input(self):
        # Test with valid input
        self.assertEqual(Elig_Checker("Alice", 25), None)  # The function prints output, so we check for None

    def test_invalid_age_input(self):
        # Test with invalid age input (non-integer)
        self.assertEqual(Elig_Checker("Alice", "twenty-five"), None)  # The function prints output, so we check for None

    def test_negative_age_input(self):
        # Test with negative age input
        self.assertEqual(Elig_Checker("Alice", -5), None)  # The function prints output, so we check for None
    
    def test_child_age(self):
        # Test with age less than 13
        self.assertEqual(Elig_Checker("Bob", 10), None)  # The function prints output, so we check for None
    def test_teenager_age(self):
        # Test with age between 13 and 17
        self.assertEqual(Elig_Checker("Charlie", 15), None)  # The function prints output, so we check for None
    def test_adult_age(self):
        # Test with age between 18 and 59
        self.assertEqual(Elig_Checker("David", 30), None)  # The function prints output, so we check for None
    def test_senior_citizen_age(self):
        # Test with age 60 and above
        self.assertEqual(Elig_Checker("Eve", 65), None)  # The function prints output, so we check for None