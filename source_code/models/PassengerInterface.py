from abc import ABC, abstractmethod

"""
Class: Passenger (Abstract Base Class)

Description:
    Represents a passenger in the travel management system. This class serves as an abstract base class
    for different types of passengers, such as StandardPassenger, GoldPassenger, and PremiumPassenger.

Attributes:
    - passenger_name: Name of the passenger.
    - passenger_number: Number assigned to the passenger.
    - passenger_mobile: Mobile number of the passenger.
    - passenger_type: Type of the passenger (e.g., Standard, Gold, Premium).
    - activities_signed_up: List of activities signed up by the passenger.

Methods:
    - __init__(self, passenger_name, passenger_number, passenger_mobile, passenger_type):
        Initializes a Passenger object with the provided details.
    
    - get_passenger_type(self):
        Returns the type of the passenger.

    - sign_up_for_activity(self, activity):
        Abstract method to be implemented by subclasses. Signs up the passenger for a specified activity.

    - __str__(self):
        Returns a string representation of the Passenger object.

Usage:
    # This class is an abstract base class and should not be instantiated directly.
    # Subclasses such as StandardPassenger, GoldPassenger, and PremiumPassenger should be used instead.

"""

class Passenger(ABC):
    def __init__(self, passenger_name, passenger_number, passenger_mobile, passenger_type):
        self.passenger_name = passenger_name
        self.passenger_number = passenger_number
        self.passenger_mobile = passenger_mobile
        self.passenger_type = passenger_type
        self.activities_signed_up = []

    @abstractmethod
    def get_passenger_type(self):
        pass

    def __str__(self):
        return f"passenger : {self.passenger_name}, activities count : {len(self.activities_signed_up)}"
