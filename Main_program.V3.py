import numpy as np
import pandas
import pandas as pd


# Functions go here

def make_statement(statement, decoration):
    print(f"{decoration * 3} {statement} {decoration * 3}")


def string_check(question, valid_answers=('yes', 'no', 'y', 'n'), num_letters=1):
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


def description():
    make_statement("Description", "📖")

    print('''

Whānau Mārama: New Zealand International Film Festival is a national event to enhance the appreciation of, \n
and engagement with, global art and culture by providing access to a diverse range of high-quality film. \n
A programme of between 150-170 features is presented in Auckland and Wellington. The Festival opens in Auckland \n
one weekend and gets underway in Wellington the next, overlapping for 10 of their respective 17-day seasons. \n
A smaller programme then travels to 11 further centres. The consolidation of several separately evolved Festivals \n
into a single event known as The New Zealand International Film Festival occurred for the first time in 2009. \n
In 2020, the Festival was rebranded Whānau Mārama: New Zealand International Film Festival.  \n
\n
In the process of purchasing your tickets from our selection of 2025 films, you will be asked to select your \n 
Tauranga Cinema after which you will see our selection of films for that Cinema. After choosing what film you'd \n 
like to see, you can choose how many tickets and what age range. You will then be shown a selection of snacks that \n
 you can preorder, and finally you will confirm or deny your purchase. Enjoy! \n

    ''')


def not_blank(question: object) -> object:
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again")


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


def treats() -> object:
    """

    :rtype: object
    """
    make_statement("Delectable Treats", "🍿")

    print()

    popcorn = string_check("Want Popcorn? ", yes_no)

    if popcorn == "yes" or popcorn == "y":
        # Display popcorn options
        print(popcorn_frame)

        popcorn_selection = num_check("Select your size: ", 1, 3)

        all_purchase_food.append(all_popcorn[popcorn_selection - 1])
        all_purchase_food_costs.append(all_popcorn_prices[popcorn_selection - 1])

        print(f"You selected {all_popcorn[popcorn_selection - 1]} Popcorn {all_popcorn_prices[popcorn_selection - 1]}")

        print()

    lollies = string_check("Want Lollies? ", yes_no)

    if lollies == "yes" or lollies == "y":
        # Display lollies options
        print(lollies_frame)

        lollies_selection = num_check("Select your size: ", 1, 3)

        all_purchase_food.append(all_lollies[lollies_selection - 1])
        all_purchase_food_costs.append(all_lollies_prices[lollies_selection - 1])

        print(f"You selected {all_lollies[lollies_selection - 1]} ${all_lollies_prices[lollies_selection - 1]}")

        print()

    drinks = string_check("Want Drinks (one size $5.00)? ", yes_no)

    if drinks == "yes" or drinks == "y":
        # Display drink options
        print(drinks_frame)

        drinks_selection = num_check("Select your drink: ", 1, 3)
        all_purchase_food.append(all_drinks[drinks_selection - 1])
        all_purchase_food_costs.append(all_drinks_prices[drinks_selection - 1])

        print(f"You selected {all_drinks[drinks_selection - 1]} $5")


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# Variables

yes_no = ["yes", "no"]
purchase_ans = ['confirm', 'cancel']

all_popcorn = ["Small", "Medium", "Large"]
all_popcorn_prices = [5, 6.5, 8]
all_lollies = ["Bag a Skittles", "Bag a Maltesers", "Box a Nerds"]
all_lollies_prices = [3, 3.5, 4]
all_drinks = ["Lemon lime and bitters", "Ginger ale", 'Lemonade']
all_drinks_prices = [5, 5, 5]

all_movies = [" It Was Just An Accident dir Jafar Panahi", "Prime Minister dir Michelle Walshe & Lindsay Utz",
              "Sentimental Value dir Joachim Trier "]

all_purchase_tickets = []
all_purchase_tickets_costs = []
all_purchase_food = []
all_purchase_food_costs = []
all_purchase_ticket_type = []

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

movies_dict = {
    'Movies': all_movies
}

all_tickets_dict = {
    'Tickets': all_purchase_tickets,
    'Ticket type': all_purchase_ticket_type,
    'Ticket Prices': all_purchase_tickets_costs
}

all_treats_dict = {
    'Treat Type': all_purchase_food,
    'Treat Prices': all_purchase_food_costs
}

# Creating DataFrame
popcorn_frame = pandas.DataFrame(popcorn_dict)
lollies_frame = pandas.DataFrame(lollies_dict)
drinks_frame = pandas.DataFrame(drinks_dict)
movies_frame = pandas.DataFrame(movies_dict)

# Rearranging index
popcorn_frame.index = np.arange(1, len(popcorn_frame) + 1)
lollies_frame.index = np.arange(1, len(lollies_frame) + 1)
drinks_frame.index = np.arange(1, len(drinks_frame) + 1)
movies_frame.index = np.arange(1, len(movies_frame) + 1)

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

# Main Routine goes here
print()
make_statement("Kia Ora and Welcome to 2025’s New Zealand International Film Festival", "🎞")

# Ask user if they want to see the instructions
# display them if necessary
print()

want_description = string_check("Would you like to see a description of the festival and the process of purchasing "
                                "tickets?")

if want_description == "yes":
    description()

# Display modified DataFrame
print("\n", df)

print()

cinema_selection = num_check("Type in your cinema selection ", 1, 5)
print()
print(f"You selected {all_cinemas[cinema_selection - 1]}")

# Display Movies

print(movies_frame)

movie_selection = num_check("Select your movie: ", 1, 3)

print(f"You selected {all_movies[movie_selection - 1]}")
print()
make_statement("Select your tickets", "🎟")

print()
kids_ticket = string_check("Are there children 7yr - 15yrs old?")

if kids_ticket == 'yes':
    num_kids_tickets = num_check("How many kids? ", 1, 5)
    all_purchase_tickets.append(num_kids_tickets)
    all_purchase_tickets_costs.append(num_kids_tickets * 10)
    all_purchase_ticket_type.append("Child")
    print(f"You have select {num_kids_tickets} kid tickets: ${num_kids_tickets * 10}")

print()

student_ticket = string_check("Are there any tertiary students? ")

if student_ticket == 'yes':
    num_student_ticket = num_check("How many students? ", 1, 5)
    all_purchase_tickets.append(num_student_ticket)
    all_purchase_tickets_costs.append(num_student_ticket * 15)
    all_purchase_ticket_type.append("Student")
    print(f"You have select {num_student_ticket} student tickets: ${num_student_ticket * 15}")

print()

adult_ticket = string_check("are there any 15yr - 64yrs olds? ")

if adult_ticket == 'yes':
    num_adult_ticket = num_check("How many adults? ", 1, 5)
    all_purchase_tickets.append(num_adult_ticket)
    all_purchase_tickets_costs.append(num_adult_ticket * 20)
    all_purchase_ticket_type.append("Adult")
    print(f"You have select {num_adult_ticket} adult tickets: ${num_adult_ticket * 20}")

print()

senior_ticket = string_check("Are there any 65+ seniors? ")

if senior_ticket == 'yes':
    num_senior_ticket = num_check("How many seniors? ", 1, 5)
    all_purchase_tickets.append(num_senior_ticket)
    all_purchase_tickets_costs.append(num_senior_ticket * 15)
    all_purchase_ticket_type.append("Senior")
    print(f"You have select {num_senior_ticket} seniors tickets: ${num_senior_ticket * 15}")

# Ask user if they want to see the instructions

print()

want_treats = string_check("Would you like some delectable treats for your film viewing?", yes_no)

if want_treats == "yes":
    treats()
else:
    all_purchase_food.append("None")
    all_purchase_food_costs.append(0.0)

print()

total_tickets_frame = pandas.DataFrame(all_tickets_dict)
total_treats_frame = pandas.DataFrame(all_treats_dict)

total_tickets_frame.index = np.arange(1, len(total_tickets_frame) + 1)

total_treats_frame.index = np.arange(1, len(total_treats_frame) + 1)

print(total_tickets_frame)

print()
print(f"Total ticket price: {sum(all_purchase_tickets_costs)}")
print()
print(total_treats_frame)
print()
print(f"Total treat price: {sum(all_purchase_food_costs)}")
print()
# total price
total_combined_costs = sum(all_purchase_food_costs + all_purchase_tickets_costs)

print(f"The total cost is ${total_combined_costs}")

print()

confirm_purchase = string_check("Do you want to confirm or cancel your order?", purchase_ans, 2)

if confirm_purchase == 'confirm':
    print(f"Your order has been placed")
    print("Thank you for your purchase! We hope you enjoy your movie going experience.")
else:
    print()
    print(f"Your order has been canceled")

print()

print("We hope you have a good day.")
