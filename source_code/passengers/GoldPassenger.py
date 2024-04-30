import sys
sys.path.append("..")
from models.PassengerInterface import Passenger

"""
Class: GoldPassenger

Description:
    Represents a gold passenger in the travel management system. Gold passengers are entitled to a 10% discount
    on the cost of activities they sign up for.

Attributes:
    - passenger_name: Name of the passenger.
    - passenger_number: Number assigned to the passenger.
    - passenger_mobile: Mobile number of the passenger.
    - passenger_balance: Balance of the passenger, used for transactions.
    - passenger_type: Type of the passenger (fixed to "Gold" for gold passengers).

Methods:
    - __init__(self, passenger_name, passenger_number, passenger_mobile, passenger_balance):
        Initializes a GoldPassenger object with the provided details.

    - sign_up_for_activity(self, activity):
        Signs up the gold passenger for the specified activity with a 10% discount on the activity cost.
        Parameters:
            - activity: Activity object representing the activity to sign up for.
        Returns:
            - True if the passenger successfully signs up for the activity, False otherwise.

Usage:
    # Create a GoldPassenger object
    gold_passenger = GoldPassenger("John Doe", "G123", "1234567890", 1000.00)
    
    # Sign up for an activity
    activity = Activity("Hiking", "Enjoy hiking in the mountains", 50.00, 10, destination)
    gold_passenger.sign_up_for_activity(activity)

"""

class GoldPassenger(Passenger):
    def __init__(self, passenger_name, passenger_number, passenger_mobile, passenger_balance):
        super().__init__(passenger_name, passenger_number, passenger_mobile, "Gold")
        self.passenger_balance = passenger_balance

    def get_passenger_type(self):
        return "Gold"

    def sign_up_for_activity(self, activity):
        discounted_cost = activity.activity_cost * 0.9
        if discounted_cost > self.passenger_balance:
            print("Insufficient balance to sign up for activity")
            return False
        self.passenger_balance -= discounted_cost
        # activity.sign_up(self)
        return True
