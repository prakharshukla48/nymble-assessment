from models.PassengerInterface import Passenger
"""
Class: PremiumPassenger

Description:
    Represents a premium passenger in the travel management system. Premium passengers have access to all activities
    for free and do not need to pay for signing up for activities.

Attributes:
    - passenger_name: Name of the passenger.
    - passenger_number: Number assigned to the passenger.
    - passenger_mobile: Mobile number of the passenger.
    - passenger_type: Type of the passenger (fixed to "Premium" for premium passengers).

Methods:
    - __init__(self, passenger_name, passenger_number, passenger_mobile):
        Initializes a PremiumPassenger object with the provided details.

    - sign_up_for_activity(self):
        Signs up the premium passenger for an activity. Since premium passengers can sign up for activities for free,
        no parameters are required.
        Returns:
            - True to indicate successful sign-up for the activity.

Usage:
    # Create a PremiumPassenger object
    premium_passenger = PremiumPassenger("Alice", "P456", "9876543210")
    
    # Sign up for an activity (no cost involved)
    premium_passenger.sign_up_for_activity()

"""

class PremiumPassenger(Passenger):

    def __init__(self, passenger_name, passenger_number, passenger_mobile):
        super().__init__(passenger_name, passenger_number, passenger_mobile, "Premium")

    def get_passenger_type(self):
        return "Premium"

    def sign_up_for_activity(self):
        return True
