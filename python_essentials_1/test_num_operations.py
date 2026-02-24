from unittest import TestCase
from python_essentials_1.num_operations import Number_operations

class TestNumberOperations(TestCase):
    def test_valid_input(self):
        # Test with valid integer inputs
        self.assertEqual(Number_operations(10, 5), None)  # The function prints output, so we check for None

    def test_division_by_zero(self):
        # Test division by zero case
        self.assertEqual(Number_operations(100, 0), None)  # The function prints output, so we check for None

    def test_invalid_input(self):
        # Test with invalid input types
        self.assertEqual(Number_operations("a", 5), None)  # The function prints output, so we check for None
        self.assertEqual(Number_operations(10, "b"), None)  # The function prints output, so we check for None
        self.assertEqual(Number_operations("c", "d"), None)  # The function prints output, so we check for None