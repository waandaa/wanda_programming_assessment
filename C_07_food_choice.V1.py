# Functions go here
import numpy as np
import pandas


def make_statement(statement, decoration):
    print(f"{decoration * 3} {statement} {decoration * 3}")


def string_check(question, valid_answers, num_letters=1):
    """Checks that users enter the full word
       or the 'n' letter/s of a word from a list of valid responses
       :rtype: object"""

    while True:

        response = input(question).lower()

        for item in valid_answers:

            # check if the response is the entire world
            if response == item:
                return item

            # check if it's the 'n' letters
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_answers}")


def num_check(question, low, high) -> object:
    """Checks users enter an integer between a low and high number"""

    error: str = f"Dduuuhh - please enter a number between {low} and {high}."

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


class Small:
    pass


def treats() -> object:
    """

    :rtype: object
    """
    make_statement("Delectable Treats", "❕")

    print()

    popcorn = string_check("Want Popcorn? ", yes_no)

    if popcorn == "yes" or popcorn == "y":
        # Display popcorn options
        print(popcorn_frame)

        popcorn_selection = num_check("Select your size: ", 1, 3)

        print(f"You selected {all_popcorn[popcorn_selection - 1]}")

        print()

    lollies = string_check("Want Lollies? ", yes_no)

    if lollies == "yes" or lollies == "y":
        # Display lollies options
        print(lollies_frame)

        lollies_selection = num_check("Select your size: ", 1, 3)

        print(f"You selected {all_lollies[lollies_selection - 1]} ${all_lollies_prices[lollies_selection - 1]}")

        print()

    drinks = string_check("Want Drinks (one size $5.00)? ", yes_no)

    if drinks == "yes" or drinks == "y":
        # Display lollies options
        print(drinks_frame)

        drinks_selection = num_check("Select your drink: ", 1, 3)

        print(f"You selected {all_drinks[drinks_selection - 1]} $5")


def not_blank(question: object) -> object:
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again")


# Variables

yes_no = ["yes", "no"]

all_popcorn = ["Small", "Medium", "Large"]
all_popcorn_prices = ["5.00", "6.50", "8.00"]
all_lollies = ["Bag a Skittles", "Bag a Maltesers", "Box a Nerds"]
all_lollies_prices = [3, 3.5, 4]
all_drinks = ["Lemon lime and bitters", "Ginger ale", 'Lemonade']
all_drinks_prices = [5, 5, 5]

# Creating a dictionary
popcorn_dict = {
    'Popcorn Sizes': all_popcorn,
    'Prices': all_popcorn_prices
}

lollies_dict = {
    'Lollies': all_lollies,
    'Prices': all_lollies_prices
}

drinks_dict = {
    'Drinks': all_drinks,
    'Prices': all_drinks_prices
}

# Creating DataFrame
popcorn_frame = pandas.DataFrame(popcorn_dict)
lollies_frame = pandas.DataFrame(lollies_dict)
drinks_frame = pandas.DataFrame(drinks_dict)

# Rearranging index
popcorn_frame.index = np.arange(1, len(popcorn_frame) + 1)
lollies_frame.index = np.arange(1, len(lollies_frame) + 1)
drinks_frame.index = np.arange(1, len(drinks_frame) + 1)

# Ask user if they want to see the instructions
# display them if necessary
print()

want_treats = string_check("Would you like some delectable treats for your film viewing?", yes_no)

if want_treats == "yes":
    treats()

print()
