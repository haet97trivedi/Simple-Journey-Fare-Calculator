"""
@author: Haet Nirav Trivedi
"""
#Imports all the necessary libraries/ Packages
from tkinter import *
import sqlite3


# Creates a Database
with sqlite3.connect("TravelPrice.db") as db:
    cursor = db.cursor()


# Create a Table - Travel
cursor.execute("""Create table IF NOT EXISTS Travel(
    age integer NOT NULL,
    ticket_price integer NOT NULL);""")

# Saves age of the passengers into database


def write_age_price():
    getage = int(age_input.get())

    if getage <= 2:
        price = 0

    elif getage >= 3 and getage <= 12:
        price = 7

    elif getage >= 66:
        price = 13

    else:
        price = 18

    cursor.execute('''
           INSERT INTO Travel(age, ticket_price) values
               (?,?);''', (getage, price))

    db.commit()
    age_input.delete(0, END)

# Display all the passenger's age


def display_age_passenger():
    display_age_show.delete(0, END)
    cursor.execute("""Select age from Travel;""")
    for ages in cursor.fetchall():
        display_age_show.insert(END, ages)


# Display all the passenger's ticket price
def display_ticket_passenger():
    display_ticket_price.delete(0, END)
    cursor.execute("""Select ticket_price from Travel;""")
    for price in cursor.fetchall():
        display_ticket_price.insert(END, price)

# Display all the passenger's ticket price


def display_total_cost():
    total = 0
    display_cost_show.delete(0, END)
    cursor.execute("""Select SUM(ticket_price) from Travel;""")
    total = cursor.fetchone()
    if total[0] is not None:
        display_cost_show.insert(0, total)


def clear_data():
    display_age_show.delete(0, END)
    display_ticket_price.delete(0, END)
    display_cost_show.delete(0, END)
    cursor.execute("""delete from Travel;""")
    db.commit()


# Creates Tkinter object
window = Tk()

# Title for the window
window.title('Simple Journey Fare Calculator')
# Sets size of the window
window.geometry("2000x2000")


# Labels
age_label = Label(text="Enter the client's age, one at a time")

age_label.place(x=30, y=30)

client_age = Label(text="Client's age in years:")

client_age.place(x=150, y=200)

ticket_price = Label(text="Price per client £:")

ticket_price.place(x=550, y=200)

cost = Label(text="Display total cost for the journey:")

cost.place(x=150, y=400)


# Takes user input
age_input = Entry(text="")

age_input.place(x=250, y=30, width=200)


#Buttons
save = Button(text="Save Age", command=write_age_price)

save.place(x=250, y=120, width=80)

clear = Button(text="Clear All", command=clear_data)

clear.place(x=350, y=120, width=80)

display_age = Button(text="Display Age", command=display_age_passenger)

display_age.place(x=50, y=250, width=80)

display_ticket = Button(text="Display ticket price",
                        command=display_ticket_passenger)

display_ticket.place(x=400, y=250)


display_cost = Button(text="Display Cost £", command=display_total_cost)

display_cost.place(x=50, y=450)


# Listbox to display all the client's age
display_age_show = Listbox()

display_age_show.place(x=150, y=220, width=100, height=150)

# Listbox to display ticket price
display_ticket_price = Listbox()

display_ticket_price.place(x=550, y=220, width=100, height=150)

# Listbox to display cost
display_cost_show = Listbox()

display_cost_show.place(x=150, y=420, width=300, height=80)


window.mainloop()

db.close()
