import unittest
from ..classes.TravelPackage import TravelPackage
from ..classes.Destination import Destination
from ..classes.Activity import Activity
from ..passengers.StandardPassenger import StandardPassenger


class TestTravelPackage(unittest.TestCase):
    def setUp(self):
        self.travel_package = TravelPackage("Test Package", 10)

    def test_add_destination(self):
        destination = Destination("Test Destination")
        self.travel_package.add_destination(destination)
        self.assertIn(destination, self.travel_package.itinerary.values())

    def test_remove_destination(self):
        destination = Destination("Test Destination")
        self.travel_package.add_destination(destination)
        self.travel_package.remove_destination("Test Destination")
        self.assertNotIn("Test Destination", self.travel_package.itinerary)

    def test_add_passenger(self):
        passenger = StandardPassenger("Alice", "123", "1234567890", 100)
        self.travel_package.add_passenger(passenger)
        self.assertIn(passenger, self.travel_package.passengers_enrolled.values())

    def test_print_itinerary(self):
        destination = Destination("Test Destination")
        activity = Activity("Test Activity", "Description", 50, 20, "Test Destination")
        destination.add_activity(activity)
        self.travel_package.add_destination(destination)
        # Redirect standard output to capture printed output
        import sys
        from io import StringIO
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            self.travel_package.print_itinerary()
            output = out.getvalue().strip()
            self.assertIn("Travel Package: Test Package", output)
            self.assertIn("Destination: Test Destination", output)
            self.assertIn("Activity: Test Activity", output)
            self.assertIn("Description: Description", output)
            self.assertIn("Cost: 50", output)
            self.assertIn("Capacity: 20", output)
        finally:
            sys.stdout = saved_stdout

    def test_print_passenger_list(self):
        passenger = StandardPassenger("Alice",
                                      "123",
                                      "1234567890",
                                      100)
        self.travel_package.add_passenger(passenger)
        # Redirect standard output to capture printed output
        import sys
        from io import StringIO
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            self.travel_package.print_passenger_list()
            output = out.getvalue().strip()
            self.assertIn("Passenger List for Travel Package: Test Package", output)
            self.assertIn("Passenger Name: Alice", output)
            self.assertIn("Passenger Number: 123", output)
            self.assertIn("Number of Passengers Enrolled: 1", output)
        finally:
            sys.stdout = saved_stdout

    def test_print_passenger_details(self):
        passenger = StandardPassenger("Alice",
                                      "123",
                                      "1234567890",
                                      100)
        destination = Destination("Test Destination")
        activity = Activity("Test Activity",
                            "Description",
                            50,
                            20,
                            "Test Destination")
        destination.add_activity(activity)
        passenger.sign_up_for_activity(activity)
        self.travel_package.add_passenger(passenger)
        # Redirect standard output to capture printed output
        import sys
        from io import StringIO
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            self.travel_package.print_passenger_details(passenger)
            output = out.getvalue().strip()
            self.assertIn("Passenger Details:", output)
            self.assertIn("Name: Alice", output)
            self.assertIn("Passenger Number: 123", output)
            self.assertIn("Activities Signed Up:", output)
        finally:
            sys.stdout = saved_stdout

    def test_print_available_activities(self):
        destination = Destination("Test Destination")
        activity = Activity("Test Activity",
                            "Description",
                            50,
                            20,
                            "Test Destination")
        destination.add_activity(activity)
        self.travel_package.add_destination(destination)
        # Redirect standard output to capture printed output
        import sys
        from io import StringIO
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            self.travel_package.print_available_activities()
            output = out.getvalue().strip()
            self.assertIn("These are Available Activities:", output)
            self.assertIn("Activity: Test Activity", output)
            self.assertIn("Destination: Test Destination", output)
            self.assertIn("Spaces Available: 20", output)
        finally:
            sys.stdout = saved_stdout

    def test_str_representation(self):
        self.assertEqual(str(self.travel_package), "package :Test Package and destination count : 0")

    def test_repr_representation(self):
        self.assertEqual(repr(self.travel_package), "package :Test Package and destination count : 0")


if __name__ == "__main__":
    unittest.main()
