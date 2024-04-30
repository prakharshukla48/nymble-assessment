""""
Class: Destination

Description:
    Represents a destination included in a travel package. Each destination has a name
    and a collection of activities available at that destination.

Attributes:
    - destination_name: Name of the destination.
    - activities: Dictionary containing activities available at the destination,
                  where keys are activity names and values are corresponding Activity objects.

Methods:
    - __init__(self, destination_name):
        Initializes a Destination object with the provided destination name.

    - add_activity(self, activity):
        Adds an activity to the list of activities available at the destination.
        Parameters:
            - activity: Activity object to be added.
        Returns:
            - The added activity.

    - remove_activity(self, activity_name):
        Removes the specified activity from the list of activities available at the destination.
        Parameters:
            - activity_name: Name of the activity to be removed.

    - __str__(self):
        Returns a string representation of the Destination object.

    - __repr__(self):
        Returns a string representation of the Destination object for debugging purposes.

Usage:
    # Create a Destination object
    destination = Destination("Beach Resort")

    # Add an activity to the destination
    activity = Activity("Scuba Diving", "Exploring underwater marine life", 100, 10, destination)
    destination.add_activity(activity)

    # Remove an activity from the destination
    destination.remove_activity("Scuba Diving")

    # Print details of the destination
    print(destination)
"""

class Destination:
    def __init__(self, destination_name):
        self.destination_name = destination_name
        self.activities = {}

    def add_activity(self, activity):
        self.activities[activity.activity_name] = activity
        return self.activities[activity.activity_name]

    def remove_activity(self, activity_name):
        del self.activities[activity_name]

    def __str__(self):
        return f"destination : {self.destination_name} and activities count : {len(self.activities)}"

    def __repr__(self):
        return f"destination : {self.destination_name} and activities count : {len(self.activities)}"
