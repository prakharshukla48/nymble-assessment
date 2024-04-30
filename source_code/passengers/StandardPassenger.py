import sys
sys.path.append("..")
from models.PassengerInterface import Passenger
"""
Class: StandardPassenger

Description:
    Represents a standard passenger in the travel management system. Standard passengers need to pay the full cost
    of activities they sign up for from their balance.

Attributes:
    - passenger_name: Name of the passenger.
    - passenger_number: Number assigned to the passenger.
    - passenger_mobile: Mobile number of the passenger.
    - passenger_balance: Balance of the passenger, used for transactions.
    - passenger_type: Type of the passenger (fixed to "Standard" for standard passengers).

Methods:
    - __init__(self, passenger_name, passenger_number, passenger_mobile, passenger_balance):
        Initializes a StandardPassenger object with the provided details.

    - sign_up_for_activity(self, activity):
        Signs up the standard passenger for the specified activity, deducting the activity cost from the passenger's
        balance. If the balance is insufficient, the sign-up fails.
        Parameters:
            - activity: Activity object representing the activity to sign up for.
        Returns:
            - True if the passenger successfully signs up for the activity, False otherwise.

Usage:
    # Create a StandardPassenger object
    standard_passenger = StandardPassenger("Bob", "S789", "5556667777", 500.00)
    
    # Sign up for an activity (deduct cost from balance)
    activity = Activity("Sightseeing", "Explore the city landmarks", 30.00, 15, destination)
    standard_passenger.sign_up_for_activity(activity)

"""

class StandardPassenger(Passenger):
    def __init__(self, passenger_name, passenger_number, passenger_mobile, passenger_balance):
        super().__init__(passenger_name, passenger_number, passenger_mobile, "Standard")
        self.passenger_balance = passenger_balance

    def get_passenger_type(self):
        return "Standard"

    def sign_up_for_activity(self, activity):
        if activity.activity_cost > self.passenger_balance:
            print("Insufficient balance to sign up for activity")
            return False
        self.passenger_balance -= activity.activity_cost
        # activity.sign_up(self)
        return True
