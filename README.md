# Simple Journey Fare Calculator

This Python script creates a GUI-based journey fare calculator using the Tkinter library. It takes the age of the client as input and calculates the fare accordingly. The fare is then stored in an SQLite database and can be displayed later on the GUI.

## Getting Started

The following libraries are required to run the code:

1. Tkinter
2. sqlite3

## Functionality

The script provides the following functionalities:

1. write_age_price(): This function takes the age of the client as input and calculates the fare according to the following criteria:

0-2 years: free
3-12 years: £7
13-65 years: £18
66+ years: £13

The fare is then stored in the Travel table in the TravelPrice.db database.

2. display_age_passenger(): This function displays the ages of all the passengers in the Travel table in the GUI.

3. display_ticket_passenger(): This function displays the fares of all the passengers in the Travel table in the GUI.

4. display_total_cost(): This function displays the total fare of all the passengers in the Travel table in the GUI.

5. clear_data(): This function clears all the data from the Travel table in the TravelPrice.db database and the GUI.

## Usage

1. Run the script in a Python IDE.
2. Enter the age of the client in the input field.
3. Click on the "Save Age" button to calculate the fare and save it in the database.
4. Click on the "Display Age" button to display the ages of all the passengers in the database.
5. Click on the "Display ticket price" button to display the fares of all the passengers in the database.
6. Click on the "Display Cost £" button to display the total fare of all the passengers in the database.
7. Click on the "Clear All" button to clear all the data from the database and the GUI.

## Conclusion

This Python script provides a simple journey fare calculator that can be used in any GUI-based Python project. The code is easy to understand and can be modified as per the user's requirements.
