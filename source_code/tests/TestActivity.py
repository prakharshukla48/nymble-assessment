import unittest
from ..classes.Activity import Activity
from ..passengers.StandardPassenger import StandardPassenger
from ..classes.TravelPackage import TravelPackage
from ..classes.Destination import Destination

class TestActivity(unittest.TestCase):
    """
    Unit tests for the Activity class.

    This class contains test cases to ensure the functionality of the Activity class methods.

    Attributes:
        destination (Destination): A Destination object for testing.
        activity (Activity): An Activity object for testing.
        passenger (StandardPassenger): A StandardPassenger object for testing.
        travel_package (TravelPackage): A TravelPackage object for testing.
    """

    def setUp(self):
        """
        Set up test data before each test case execution.

        This method initializes test objects required for each test case.
        """
        self.destination = Destination("Test Destination")
        self.activity = Activity("Test Activity",
                                 "Description",
                                 50,
                                 20,
                                 self.destination)
        self.passenger = StandardPassenger("Alice",
                                           "123",
                                           "1234567890",
                                           100)
        self.travel_package = TravelPackage("Test Package", 10)

    def test_sign_up_success(self):
        """
        Test case to ensure successful sign-up for an activity.

        This method tests the sign_up method of the Activity class when the sign-up is successful.
        """
        result = self.activity.sign_up(self.passenger, self.travel_package)
        self.assertTrue(result)
        self.assertIn(self.passenger, self.activity.passengers_signed_up)
        self.assertIn(self.passenger, self.travel_package.passengers_enrolled.values())
        self.assertIn(self.activity, self.passenger.activities_signed_up)

    def test_sign_up_failure_capacity(self):
        """
        Test case to ensure failure of sign-up due to activity capacity limit.

        This method tests the sign_up method of the Activity class when the activity's capacity limit is reached.
        """
        for _ in range(20):
            self.activity.sign_up(StandardPassenger("Passenger",
                                                    "1",
                                                    "1234567890",
                                                    100),
                                  self.travel_package)
        result = self.activity.sign_up(self.passenger, self.travel_package)
        self.assertFalse(result)
        self.assertNotIn(self.passenger, self.activity.passengers_signed_up)
        self.assertNotIn(self.passenger, self.travel_package.passengers_enrolled.values())
        self.assertNotIn(self.activity, self.passenger.activities_signed_up)

    def test_sign_up_failure_package_capacity(self):
        """
        Test case to ensure failure of sign-up due to travel package capacity limit.

        This method tests the sign_up method of the Activity class when the travel package's capacity limit is reached.
        """
        for _ in range(10):
            self.travel_package.add_passenger(StandardPassenger("Passenger",
                                                                "1",
                                                                "1234567890",
                                                                100))
        result = self.activity.sign_up(self.passenger, self.travel_package)
        self.assertTrue(result)
        self.assertIn(self.passenger, self.activity.passengers_signed_up)
        self.assertIn(self.passenger, self.travel_package.passengers_enrolled.values())
        self.assertIn(self.activity, self.passenger.activities_signed_up)

    def test_str_representation(self):
        """
        Test case to ensure correct string representation of the Activity object.

        This method tests the __str__ method of the Activity class to ensure correct string representation.
        """
        self.assertEqual(str(self.activity), "Activity : Test Activity, passengers : []")

    def test_repr_representation(self):
        """
        Test case to ensure correct representation of the Activity object.

        This method tests the __repr__ method of the Activity class to ensure correct representation.
        """
        self.assertEqual(repr(self.activity), "Activity : Test Activity, passengers : []")


if __name__ == "__main__":
    unittest.main()
