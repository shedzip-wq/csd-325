# Sheridan Dela Cruz
# May 2, 2026
# Module 7.2

# Tests the city_country function to ensure it returns the correct formatted string.

import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):
    """Tests for the city_country function."""

    def test_city_country(self):
        """Check that city and country are formatted correctly."""
        result = city_country("Reykjavik", "Iceland")
        self.assertEqual(result, "Reykjavik, Iceland")

# Runs the tests when the file is executed.
unittest.main()
