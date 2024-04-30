import unittest
from ..passengers.GoldPassenger import GoldPassenger
from ..classes.Activity import Activity

class TestGoldPassenger(unittest.TestCase):
    """
    Unit tests for the GoldPassenger class.

    This class contains test cases to ensure the functionality of the GoldPassenger class methods.

    Attributes:
        gold_passenger (GoldPassenger): A GoldPassenger object for testing.
    """

    def setUp(self):
        """
        Set up test data before each test case execution.

        This method initializes a test GoldPassenger object required for each test case.
        """
        self.gold_passenger = GoldPassenger("Bob",
                                            "456",
                                            "9876543210",
                                            150)

    def test_balance(self):
        """
        Test case to ensure correct initialization of passenger balance.

        This method tests whether the initial balance of the GoldPassenger object is set correctly.
        """
        self.assertEqual(self.gold_passenger.passenger_balance, 150)

    def test_sign_up_for_activity_sufficient_balance(self):
        """
        Test case for successful signup for an activity with sufficient balance.

        This method tests the sign_up_for_activity method of the GoldPassenger class when the balance is sufficient.
        """
        activity = Activity("Test Activity",
                            "Description",
                            50,
                            20,
                            "Test Destination")
        self.assertTrue(self.gold_passenger.sign_up_for_activity(activity))
        self.assertEqual(self.gold_passenger.passenger_balance, 105)

    def test_sign_up_for_activity_insufficient_balance(self):
        """
        Test case for failed signup for an activity with insufficient balance.

        This method tests the sign_up_for_activity method of the GoldPassenger class when the balance is insufficient.
        """
        activity = Activity("Test Activity",
                            "Description",
                            200,
                            20,
                            "Test Destination")
        self.assertFalse(self.gold_passenger.sign_up_for_activity(activity))
        self.assertEqual(self.gold_passenger.passenger_balance, 150)

if __name__ == "__main__":
    unittest.main()
