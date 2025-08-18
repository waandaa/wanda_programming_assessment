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


all_cinemas = [" Event Tauranga Crossing", "Event Tauranga Central", "Luxe Tauranga Central", "Luxe Papamoa",
               "United Bayfair"]

# Creating a dictionary
cinema_dict = {
    'Cinemas': all_cinemas
}

# Creating DataFrame
df = pd.DataFrame(cinema_dict)

# Rearranging index
df.index = np.arange(1, len(df) + 1)

# Display modified DataFrame
print("\n", df)

print()

cinema_selection = num_check("Type in your cinema selection ", 1, 5)

print(f"You selected {all_cinemas[cinema_selection - 1]}")
