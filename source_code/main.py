# Importing the TravelApp class from the TravelApp module
from TravelApp import TravelApp

# Main function to run the travel agency application
def main():
    # Displaying welcome message
    print("Welcome to the travel agency App")

    # Creating an instance of the TravelApp class
    travel_app = TravelApp()

    # Main loop for the application
    while True:
        # Prompting the user to choose a role or exit
        print("Enter 'ADMIN' to login as agency manager, 'PASSENGER' to login as passenger or 'EXIT' to close the app")
        user = input()

        # Exiting the application if user chooses to exit
        if user == "EXIT":
            print("Closing the app")
            break

        # Handling admin actions
        elif user == "ADMIN":
            try:
                # Prompting the admin to add a new package or edit an existing one
                print("Enter 'NEW' to add a new package or name of the existing package to edit it")
                inp = input()

                # Adding a new package
                if inp == "NEW":
                    print("Please Enter package name and its capacity after ','")
                    package_name, passenger_capacity = input().strip().split(",")
                    passenger_capacity = int(passenger_capacity)
                    package = travel_app.add_package(package_name=package_name, passenger_capacity=passenger_capacity)
                else:
                    package = travel_app.packages.get(inp)
                    if not package:
                        print("No such package exist, please try again")
                        continue

                # Prompting to add or remove a destination from the package itinerary
                print(f"Enter ADD and name of destination after ','  to add destination to "
                      f"the package or REMOVE and name after ',' if it exists for {package.package_name} ")
                operation, destination_name = input().split(",")
                if operation == "ADD":
                    travel_app.add_itinerary(destination_name=destination_name, package=package)
                    print(f"{destination_name} added successfully to package {package.package_name}")
                else:
                    travel_app.remove_itinerary(destination_name=destination_name, package=package)
                    print(f"{destination_name} removed successfully from package {package.package_name}")

                # Prompting to add or remove activities for a destination
                print(f"Enter ADD and destination name with ','  separation to add activities for a destination or"
                      f" REMOVE and destination name with ','  separation to remove from {package.itinerary}")
                operation, destination_name = input().split(',')
                travel_destination = package.itinerary.get(destination_name, None)
                if not travel_destination:
                    print("travel destination not found , taking you to main menu ")
                    continue
                if operation == "ADD":
                    print(f"Enter details like (name, description, cost, capacity) each on new line for the activity"
                          f" to add for {destination_name}")
                    activity = travel_app.add_destination_activity(activity_name=input(),
                                                                   activity_description=input(),
                                                                   activity_cost=float(input()),
                                                                   activity_capacity=int(input()),
                                                                   activity_destination=travel_destination
                                                                   )
                    print(f"{activity} added successfully to {travel_destination}")
                else:
                    print(f"Enter name of activity to delete from the destination {destination_name}")
                    activity_name = input()
                    travel_app.remove_destination_activity(
                        activity_name=activity_name,
                        activity_destination=travel_destination
                    )
                    print(f"{activity_name} removed successfully")
            except ValueError:
                print("Try again and enter details accordingly", ValueError)
                continue

        # Handling passenger actions
        elif user == "PASSENGER":
            # Prompting the passenger to enter their mobile number
            print("Please Enter Your Mobile Number to continue")
            user_mobile = input()
            passenger = travel_app.passengers.get(user_mobile, None)
            if not passenger:
                # Prompting the passenger to enter their details and choose a membership type
                print("Please Enter your name and after ',' separation Enter '100' to pay and  become standard member,"
                      " '500' to pay and become gold member and '2000' to pay and become premium member  ")
                try:
                    passenger_name, amount = input().split(",")
                except ValueError:
                    continue
                if amount == '100':
                    print(f"Thanks {passenger_name} for joining as a standard member, your balance is 100 rupees")
                    passenger = travel_app.add_standard_passenger(passenger_name=passenger_name,
                                                                  passenger_balance=100, passenger_mobile=user_mobile
                                                                 )
                elif amount == '500':
                    print(f"Thanks {passenger_name} for joining as a Gold member, your balance is 500 rupees")
                    passenger = travel_app.add_gold_passenger(passenger_name=passenger_name,
                                                              passenger_balance=500,  passenger_mobile=user_mobile
                                                              )
                elif amount == '2000':
                    print(f"Thanks {passenger_name} for joining as a premium member")
                    passenger = travel_app.add_premium_passenger(
                                                                 passenger_name=passenger_name,
                                                                 passenger_mobile=user_mobile
                                                                )
                else:
                    print("invalid Input")
            else:
                print(f"WELCOME {passenger.passenger_name}")
                if passenger.get_passenger_type != "Premium":
                     print(f"you current balance is {passenger.passenger_balance}")

            # Prompting the passenger to choose an action
            while True:
                try:
                    print("Please enter the name of the package you are interested in")
                    print("package_names", travel_app.packages.values())
                    package = travel_app.packages.get(input(), None)
                    if not package:
                        print("package does not exist, please try again")
                        break
                    print("Enter 'ITINERARY' to get the itinerary details of the package or"
                          " 'PASSENGERS' to get the Passengers details or "
                          "enter passenger mobile to get details of individual passenger or"
                          " 'ACTIVITY'  to get activity details or "
                          "'ACTIVITY_SIGNUP if you want to signup for a activity' or"
                          "'BACK' to go back .")
                    user_input = input()
                    if user_input == 'ITINERARY':
                        package.print_itinerary()
                    elif user_input == 'PASSENGERS':
                        package.print_passenger_list()
                    elif user_input == 'ACTIVITY':
                        package.print_available_activities()
                    elif user_input == 'ACTIVITY_SIGNUP':

                        print("Please Enter destination_name and after"
                              " ',' enter activity_name you want to signup for")
                        destination_name,  activity_name = input().split(",")
                        print("activities", package.itinerary[destination_name].activities)
                        if package.itinerary[destination_name].activities[activity_name].sign_up(
                                passenger=passenger, package=package):
                            print(f"you have signed up for the activity {activity_name}. ")
                            if passenger.get_passenger_type != "Premium":
                                print(f"{passenger.passenger_name} your "
                                      f"current balance is {passenger.passenger_balance}")

                        else:
                            print("Not enough capacity available for this activity")
                        continue
                    elif user_input == "BACK":
                        break
                    else:
                        package.print_passenger_details(passenger=travel_app.passengers[user_input])
                    break
                except ValueError:
                    print("please input values correctly and correct line", ValueError)
                    continue
        else:
            print("Invalid Input , Please try again")
            continue

# Running the main function if the module is executed directly
if __name__ == "__main__":
    main()
