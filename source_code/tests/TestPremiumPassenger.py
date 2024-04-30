import unittest
from ..passengers.PremiumPassenger import PremiumPassenger
from ..classes.Activity import Activity

class TestPremiumPassenger(unittest.TestCase):
    """
    Unit tests for the PremiumPassenger class.

    This class contains test cases to ensure the functionality of the PremiumPassenger class methods.

    Attributes:
        premium_passenger (PremiumPassenger): A PremiumPassenger object for testing.
    """

    def setUp(self):
        """
        Set up test data before each test case execution.

        This method initializes a test PremiumPassenger object required for each test case.
        """
        self.premium_passenger = PremiumPassenger("Charlie",
                                                  "789",
                                                  "9876543210")

    def test_get_passenger_type(self):
        """
        Test case to ensure correct retrieval of passenger type.

        This method tests whether the get_passenger_type method of the PremiumPassenger class returns 'Premium'.
        """
        self.assertEqual(self.premium_passenger.get_passenger_type(), "Premium")

    def test_sign_up_for_activity(self):
        """
        Test case for signing up for an activity as a premium passenger.

        This method tests the sign_up_for_activity method of the PremiumPassenger class.
        """
        activity = Activity("Test Activity",
                            "Description",
                            50,
                            20,
                            "Test Destination")
        self.assertTrue(self.premium_passenger.sign_up_for_activity(activity))

if __name__ == "__main__":
    unittest.main()
