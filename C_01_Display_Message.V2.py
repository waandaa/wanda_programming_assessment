# Functions go here
def make_statement(statement: object, decoration: object) -> object:
    """Emphasises headings by adding decoration
    at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


# Main Routine goes here
print()
make_statement("Kia Ora and Welcome to 2025’s New Zealand International Film Festival", ":)")
