import unittest
from python_essentials_1.user_info import User_Info

class TestUserInfo(unittest.TestCase):
    def test_valid_input(self):
        # Test with valid input
        self.assertEqual(User_Info("John", "Doe", 30), None)  # The function prints output, so we check for None

    def test_invalid_age_input(self):
        # Test with invalid age input (non-integer)
        self.assertEqual(User_Info("John", "Doe", "thirty"), None)  # The function prints output, so we check for None

    def test_negative_age_input(self):
        # Test with negative age input
        self.assertEqual(User_Info("John", "Doe", -5), None)  # The function prints output, so we check for None