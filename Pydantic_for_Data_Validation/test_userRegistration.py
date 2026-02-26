import unittest
from Pydantic_for_Data_Validation.userRegistration import UserRegister
class TestUserRegistration(unittest.TestCase):
    def test_valid_user_registration(self):
        user = UserRegister(username="john_doe", email="john_doe@example.com", age=25)
        self.assertEqual(user.username, "john_doe")
        self.assertEqual(user.email, "john_doe@example.com")
        self.assertEqual(user.age, 25)
    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            UserRegister(username="john_doe", email="invalid_email", age=25)
    def test_short_username(self):
        with self.assertRaises(ValueError):
            UserRegister(username="john", email="john@example.com", age=25)
    def test_underage_user(self):
        with self.assertRaises(ValueError):
            UserRegister(username="john_doe", email="john_doe@example.com", age=15)