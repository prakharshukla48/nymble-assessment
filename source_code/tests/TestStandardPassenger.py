import unittest
from ..passengers.StandardPassenger import StandardPassenger
from ..classes.Activity import Activity

class TestStandardPassenger(unittest.TestCase):
    """
    Unit tests for the StandardPassenger class.

    This class contains test cases to ensure the functionality of the StandardPassenger class methods.

    Attributes:
        standard_passenger (StandardPassenger): A StandardPassenger object for testing.
    """

    def setUp(self):
        """
        Set up test data before each test case execution.

        This method initializes a test StandardPassenger object required for each test case.
        """
        self.standard_passenger = StandardPassenger("Alice",
                                                    "123",
                                                    "1234567890",
                                                    100)

    def test_balance(self):
        """
        Test case to check the initial balance of the standard passenger.

        This method verifies that the initial balance of the StandardPassenger object is set correctly.
        """
        self.assertEqual(self.standard_passenger.passenger_balance, 100)

    def test_sign_up_for_activity_sufficient_balance(self):
        """
        Test case for signing up for an activity with sufficient balance.

        This method tests whether a standard passenger can successfully sign up for an activity when the balance is sufficient.
        """
        activity = Activity("Test Activity",
                            "Description",
                            50,
                            20,
                            "Test Destination")
        self.assertTrue(self.standard_passenger.sign_up_for_activity(activity))
        self.assertEqual(self.standard_passenger.passenger_balance, 50)

    def test_sign_up_for_activity_insufficient_balance(self):
        """
        Test case for signing up for an activity with insufficient balance.

        This method tests whether a standard passenger fails to sign up for an activity when the balance is insufficient.
        """
        activity = Activity("Test Activity",
                            "Description",
                            150,
                            20,
                            "Test Destination")
        self.assertFalse(self.standard_passenger.sign_up_for_activity(activity))
        self.assertEqual(self.standard_passenger.passenger_balance, 100)

if __name__ == "__main__":
    unittest.main()
