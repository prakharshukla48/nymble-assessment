from classes.Destination import Destination
from classes.Activity import Activity
from passengers.GoldPassenger import GoldPassenger
from passengers.PremiumPassenger import PremiumPassenger
from passengers.StandardPassenger import StandardPassenger
from classes.TravelPackage import TravelPackage

"""
Class: TravelApp

Description:
    Represents a travel application that manages travel packages, destinations, activities, and passengers.

Attributes:
    - packages: Dictionary containing travel packages, where keys are package names and values are TravelPackage objects.
    - passengers: Dictionary containing passengers, where keys are passenger mobile numbers and values are Passenger objects.

Methods:
    - __init__(self):
        Initializes a TravelApp object with empty dictionaries for packages and passengers.

    - add_package(self, package_name, passenger_capacity):
        Adds a new travel package to the application.
        Parameters:
            - package_name: Name of the travel package.
            - passenger_capacity: Maximum number of passengers the package can accommodate.
        Returns:
            - The created TravelPackage object.

    - add_itinerary(self, destination_name, package):
        Adds a new destination to a travel package's itinerary.
        Parameters:
            - destination_name: Name of the destination to add.
            - package: TravelPackage object to add the destination to.

    - remove_itinerary(self, destination_name, package):
        Removes a destination from a travel package's itinerary.
        Parameters:
            - destination_name: Name of the destination to remove.
            - package: TravelPackage object to remove the destination from.

    - add_destination_activity(self, activity_name, activity_description, activity_cost, activity_capacity, activity_destination):
        Adds a new activity to a destination.
        Parameters:
            - activity_name: Name of the activity.
            - activity_description: Description of the activity.
            - activity_cost: Cost of the activity.
            - activity_capacity: Maximum capacity of the activity.
            - activity_destination: Destination object to add the activity to.
        Returns:
            - The created Activity object.

    - remove_destination_activity(self, activity_name, activity_destination):
        Removes an activity from a destination.
        Parameters:
            - activity_name: Name of the activity to remove.
            - activity_destination: Destination object to remove the activity from.

    - add_standard_passenger(self, passenger_name, passenger_balance, passenger_mobile):
        Adds a new standard passenger to the application.
        Parameters:
            - passenger_name: Name of the passenger.
            - passenger_balance: Initial balance of the passenger.
            - passenger_mobile: Mobile number of the passenger.
        Returns:
            - The created StandardPassenger object.

    - add_gold_passenger(self, passenger_name, passenger_balance, passenger_mobile):
        Adds a new gold passenger to the application.
        Parameters:
            - passenger_name: Name of the passenger.
            - passenger_balance: Initial balance of the passenger.
            - passenger_mobile: Mobile number of the passenger.
        Returns:
            - The created GoldPassenger object.

    - add_premium_passenger(self, passenger_name, passenger_mobile):
        Adds a new premium passenger to the application.
        Parameters:
            - passenger_name: Name of the passenger.
            - passenger_mobile: Mobile number of the passenger.
        Returns:
            - The created PremiumPassenger object.

    - __str__(self):
        Returns a string representation of the TravelApp object, including the total number of packages and passengers.

Usage:
    # Create a TravelApp object
    travel_app = TravelApp()

    # Add a new travel package
    package = travel_app.add_package("Europe Tour", 50)

    # Add a destination to the travel package
    travel_app.add_itinerary("Paris", package)

    # Add an activity to the destination
    activity = travel_app.add_destination_activity("Sightseeing", "Explore the city landmarks", 30.00, 15, destination)

    # Add a passenger to the travel app
    passenger = travel_app.add_standard_passenger("Alice", 500.00, "1234567890")

"""

class TravelApp:
    def __init__(self):
        self.packages = {}
        self.passengers = {}

    def add_package(self, package_name, passenger_capacity):
        self.packages[package_name] = (TravelPackage(package_name, passenger_capacity))
        return self.packages[package_name]

    def add_itinerary(self, destination_name, package):
        # defaulting maximum 3 itinerary per pacakge
        package.add_destination(Destination(destination_name=destination_name))

    def remove_itinerary(self, destination_name, package):
        package.remove_destination(destination_name)

    def add_destination_activity(self, activity_name,
                                 activity_description, activity_cost, activity_capacity, activity_destination):
        return activity_destination.add_activity(activity=Activity(activity_name=activity_name,
                                                 activity_description=activity_description,
                                                 activity_cost=activity_cost,
                                                 activity_capacity=activity_capacity,
                                                 activity_destination=activity_destination))

    def remove_destination_activity(self, activity_name, activity_destination):
        activity_destination.remove_activity(activity_name=activity_name)

    def add_standard_passenger(self,  passenger_name, passenger_balance, passenger_mobile):
        self.passengers[passenger_mobile] = StandardPassenger(passenger_name=passenger_name,
                                                              passenger_number=len(self.passengers)+1,
                                                              passenger_mobile=passenger_mobile,
                                                              passenger_balance=passenger_balance)
        return self.passengers[passenger_mobile]

    def add_gold_passenger(self, passenger_name, passenger_balance, passenger_mobile):
        self.passengers[passenger_mobile] = GoldPassenger(passenger_name=passenger_name,
                                                          passenger_number=len(self.passengers) + 1,
                                                          passenger_mobile=passenger_mobile,
                                                          passenger_balance=passenger_balance)
        return self.passengers[passenger_mobile]

    def add_premium_passenger(self, passenger_name, passenger_mobile):
        self.passengers[passenger_mobile] = PremiumPassenger(passenger_name=passenger_name,
                                                             passenger_number=len(self.passengers) + 1,
                                                             passenger_mobile=passenger_mobile
                                                             )
        return self.passengers[passenger_mobile]

    def __str__(self):
        return f"Total packages are {len(self.packages)} and total passengers are  {len(self.passengers)}"
