# Functions go here

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


# Main Routine goes here
print()
make_statement("How many tickets would you like", "?")

print()

kids_selection = num_check("7yr - 15yrs old ($10.00):", 0, 5)

print(f"You selected {kids_selection}")

print()

adults_selection = num_check("15yr - 64yrs old ($20.00):", 0, 5)

print(f"You selected {adults_selection}")

print()

seniors_selection = num_check("65yr old+ ($15.00):", 0, 5)

print(f"You selected {seniors_selection}")

print()

students_selection = num_check("Student tertiary ($15.00):", 0, 5)

print(f"You selected {students_selection}")

print()

print(f"You have selected: Kids tickets: {kids_selection - 0}, Adults tickets: {adults_selection - 0} "
      f", Senior tickets: {seniors_selection - 0} and Student tickets: {students_selection - 0}")
