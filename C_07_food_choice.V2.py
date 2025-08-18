# Importing pandas package
import pandas as pd

# Importing numpy package
import numpy as np


# lists to hold pass details


# Functions go here
def num_check(question, low, high):
    """Checks users enter an integer between a low and high number"""

    error = f"Dduuuhh - please enter a number between {low} and {high}."

    while True:
        try:

            # Change the response to an integer and check that it's more than zero

            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


all_popcorn = ["Small ($5.00)", "Medium ($6.50)", "Large ($8.00)", ]

# Creating a dictionary
popcorn_dict = {
    'Popcorn': all_popcorn
}

# Creating DataFrame
df = pd.DataFrame(popcorn_dict)

# Rearranging index
df.index = np.arange(1, len(df) + 1)

# Display modified DataFrame
print("\n", df)

print()

popcorn_selection = num_check("Type in your popcorn selection ", 1, 5)

print(f"You selected {all_popcorn[popcorn_selection - 1]}")


# Functions go here
def num_check(question, low, high):
    """Checks users enter an integer between a low and high number"""

    error = f"Dduuuhh - please enter a number between {low} and {high}."

    while True:
        try:

            # Change the response to an integer and check that it's more than zero

            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


all_lollies = ["Bag a Skittles ($3.00)", "Bag a Maltesers ($3.50)", "Box a Nerds ($4.00)", ]

# Creating a dictionary
lollies_dict = {
    'Lollies': all_lollies
}

# Creating DataFrame
df = pd.DataFrame(lollies_dict)

# Rearranging index
df.index = np.arange(1, len(df) + 1)

# Display modified DataFrame
print("\n", df)

print()

lollies_selection = num_check("Type in your lolly selection ", 1, 5)

print(f"You selected {all_lollies[lollies_selection - 1]}")


# Functions go here
def num_check(question, low, high):
    """Checks users enter an integer between a low and high number"""

    error = f"Dduuuhh - please enter a number between {low} and {high}."

    while True:
        try:

            # Change the response to an integer and check that it's more than zero

            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


all_drinks = ["Lemon lime and bitters", "Ginger ale", "Lemonade", ]

# Creating a dictionary
drinks_dict = {
    'Drinks (one size $5.00)': all_drinks
}

# Creating DataFrame
df = pd.DataFrame(drinks_dict)

# Rearranging index
df.index = np.arange(1, len(df) + 1)

# Display modified DataFrame
print("\n", df)

print()

drinks_selection = num_check("Type in your Drink selection ", 1, 5)

print(f"You selected {all_drinks[drinks_selection - 1]}")

print()

print(f"You selected {all_drinks[drinks_selection - 1]} , {all_lollies[lollies_selection - 1]} and"
      f" {all_popcorn[popcorn_selection - 1]}")
