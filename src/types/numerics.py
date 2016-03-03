__author__ = 'Antony Cherepanov'


def auto_type_change():
    """ Python automatically changes type of a variable. Also it's automatically provides extra precision
     for large numbers.
    """

    value = 62
    print("This value can hold char variable: " + str(value))

    value = 3 * (10 ** 5)
    print("Now it's int: " + str(value))

    value = 2 ** 1000
    print("Very, very long number: " + str(len(str(value))) + " - number of digits")


auto_type_change()