import unittest
from ..classes.Destination import Destination
from ..classes.Activity import Activity

class TestDestination(unittest.TestCase):
    """
    Unit tests for the Destination class.

    This class contains test cases to ensure the functionality of the Destination class methods.

    Attributes:
        destination (Destination): A Destination object for testing.
    """

    def setUp(self):
        """
        Set up test data before each test case execution.

        This method initializes a test Destination object required for each test case.
        """
        self.destination = Destination("Test Destination")

    def test_add_activity(self):
        """
        Test case to ensure successful addition of an activity to the destination.

        This method tests the add_activity method of the Destination class.
        """
        activity = Activity("Test Activity",
                            "Description",
                            50,
                            20,
                            "Test Destination")
        self.destination.add_activity(activity)
        self.assertIn(activity, self.destination.activities.values())

    def test_remove_activity(self):
        """
        Test case to ensure successful removal of an activity from the destination.

        This method tests the remove_activity method of the Destination class.
        """
        activity = Activity("Test Activity",
                            "Description",
                            50,
                            20,
                            "Test Destination")
        self.destination.add_activity(activity)
        self.destination.remove_activity("Test Activity")
        self.assertNotIn("Test Activity", self.destination.activities)

    def test_str_representation(self):
        """
        Test case to ensure correct string representation of the Destination object.

        This method tests the __str__ method of the Destination class to ensure correct string representation.
        """
        self.assertEqual(str(self.destination), "destination : Test Destination and activities count : 0")

    def test_repr_representation(self):
        """
        Test case to ensure correct representation of the Destination object.

        This method tests the __repr__ method of the Destination class to ensure correct representation.
        """
        self.assertEqual(repr(self.destination), "destination : Test Destination and activities count : 0")

if __name__ == "__main__":
    unittest.main()
