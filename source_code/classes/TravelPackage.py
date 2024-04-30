"""
Class: TravelPackage

Description:
    Represents a travel package offered by a travel agency. Each package has a name,
    passenger capacity, an itinerary (list of destinations), and a list of enrolled passengers.

Attributes:
    - package_name: Name of the travel package.
    - passenger_capacity: Maximum number of passengers allowed for the package.
    - itinerary: Dictionary containing destinations in the package,
                 where keys are destination names and values are Destination objects.
    - passengers_enrolled: Dictionary containing enrolled passengers,
                           where keys are passenger mobile numbers and values are Passenger objects.

Methods:
    - __init__(self, package_name, passenger_capacity):
        Initializes a TravelPackage object with the provided package name and passenger capacity.

    - add_destination(self, destination):
        Adds a destination to the itinerary of the travel package.
        Parameters:
            - destination: Destination object to be added.

    - remove_destination(self, destination_name):
        Removes the specified destination from the itinerary of the travel package.
        Parameters:
            - destination_name: Name of the destination to be removed.

    - add_passenger(self, passenger):
        Adds a passenger to the list of enrolled passengers for the travel package,
        if the package is not already full.

    - print_itinerary(self):
        Prints the itinerary of the travel package, including destinations and activities available at each destination.

    - print_passenger_list(self):
        Prints the list of passengers enrolled in the travel package.

    - print_passenger_details(self, passenger):
        Prints details of a specific passenger, including name, number, balance (if applicable),
        and activities signed up for.

    - print_available_activities(self):
        Prints the details of available activities in the travel package, including destination,
        activity name, and spaces available.

    - __str__(self):
        Returns a string representation of the TravelPackage object.

    - __repr__(self):
        Returns a string representation of the TravelPackage object for debugging purposes.

Usage:
    # Create a TravelPackage object
    travel_package = TravelPackage("Summer Vacation", 50)

    # Add destinations to the travel package itinerary
    destination1 = Destination("Beach Resort")
    destination2 = Destination("Mountain Resort")
    travel_package.add_destination(destination1)
    travel_package.add_destination(destination2)

    # Remove a destination from the itinerary
    travel_package.remove_destination("Mountain Resort")

    # Add a passenger to the travel package
    travel_package.add_passenger(passenger)

    # Print itinerary, passenger list, etc.
    travel_package.print_itinerary()
    travel_package.print_passenger_list()
    travel_package.print_available_activities()
"""

class TravelPackage:
    def __init__(self, package_name, passenger_capacity):
        self.package_name = package_name
        self.passenger_capacity = passenger_capacity
        self.itinerary = {}
        self.passengers_enrolled = {}

    def add_destination(self, destination):
        self.itinerary[destination.destination_name] = destination

    def remove_destination(self, destination_name):
        del self.itinerary[destination_name]

    def add_passenger(self, passenger):
        if len(self.passengers_enrolled) >= self.passenger_capacity:
            print("Travel package is full. Cannot enroll more passengers.")
            return
        self.passengers_enrolled[passenger.passenger_mobile] = passenger

    def print_itinerary(self):
        print("Travel Package:", self.package_name)
        for destination in self.itinerary.values():
            print("Destination:", destination.destination_name)
            for activity in destination.activities.values():
                print("Activity:", activity.activity_name)
                print("Description:", activity.activity_description)
                print("Cost:", activity.activity_cost)
                print("Capacity:", activity.activity_capacity)

    def print_passenger_list(self):
        print("Passenger List for Travel Package:", self.package_name)
        print("Passenger Capacity:", self.passenger_capacity)
        print("Number of Passengers Enrolled:", len(self.passengers_enrolled))
        for passenger in self.passengers_enrolled.values():
            print("Passenger Name:", passenger.passenger_name)
            print("Passenger Number:", passenger.passenger_number)

    def print_passenger_details(self, passenger):
        print("Passenger Details:")
        print("Name:", passenger.passenger_name)
        print("Passenger Number:", passenger.passenger_number)
        if passenger.passenger_type in ['standard', 'gold']:
            print("Balance:", passenger.passenger_balance)
        print("Activities Signed Up:")
        for activity in passenger.activities_signed_up:
            print("Activity:", activity.activity_name)
            print("Destination:", activity.activity_destination.destination_name)
            print("Price Paid:", activity.activity_cost)

    def print_available_activities(self):
        print("These are Available Activities:")
        flag = True
        for destination in self.itinerary.values():
            for activity in destination.activities.values():
                if len(activity.passengers_signed_up) < activity.activity_capacity:
                    flag = False
                    print("Activity:", activity.activity_name)
                    print("Destination:", activity.activity_destination)
                    print("Spaces Available:", activity.activity_capacity - len(activity.passengers_signed_up))
        if flag:
            print("No Activities available")

    def __str__(self):
        return f"package :{self.package_name} and destination count : {len(self.itinerary)}"

    def __repr__(self):
        return f"package :{self.package_name} and destination count : {len(self.itinerary)}"
