# Functions go here
import pandas
import pandas as np


def make_statement(statement, decoration):
    print(f"{decoration * 3} {statement} {decoration * 3}")


def string_check(question: object, valid_answers: object = ('yes', 'no'), num_letters: object = 1) -> object:
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


movies_dict = {
    'Movies'
}

# Creating DataFrame
movies_frame = pandas.DataFrame(movies_dict)

# Rearranging index)
movies_frame.index = np.arange(1, len(movies_frame) + 1)

# lists to hold cinema details
all_cinemas = [" Event Tauranga Crossing", "Event Tauranga Central", "Luxe Tauranga Central", "Luxe Papamoa", "United "
                                                                                                              "Bayfair"]

mini_cinema_dict = {
    'Cinemas': all_cinemas

}

# create dataframe / table from dictionary
mini_cinema_frame = pandas.DataFrame(mini_cinema_dict)

print(mini_cinema_frame)
print()

all_movies = [" It Was Just An Accident dir Jafar Panahi", "Prime Minister dir Michelle Walshe & Lindsay Utz",
              "Sentimental Value dir Joachim Trier "]

# Display Movies

print(movies_frame)

movie_selection = num_check("Select your movie: ", 1, 3)

print(f"You selected {all_movies[movie_selection - 1]}")
