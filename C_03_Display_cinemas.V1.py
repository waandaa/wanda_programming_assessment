import pandas

# lists to hold pass details
all_cinemas = [" Event Tauranga Crossing", "Event Tauranga Central", "Luxe Tauranga Central", "Luxe Papamoa", "United "
                                                                                                              "Bayfair"]

mini_cinema_dict = {
    'Cinemas': all_cinemas


}

# create dataframe / table from dictionary
mini_cinema_frame = pandas.DataFrame(mini_cinema_dict)


print(mini_cinema_frame)
print()

cinema_selection = input("Type in your cinema selection ")

print(f"You selected {cinema_selection}")
