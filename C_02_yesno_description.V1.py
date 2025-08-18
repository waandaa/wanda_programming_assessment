# Functions go here

def make_statement(statement, decoration):
    print(f"{decoration * 3} {statement} {decoration * 3}")


def string_check(question, valid_answers=('yes', 'no'), num_letters=1):
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
    make_statement("Description", "❕")

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


# Ask user if they want to see the instructions
# display them if necessary
print()

want_description = string_check("Would you like to see a description of the festival and the process of purchasing "
                                "tickets?")

if want_description == "yes":
    description()

print()
