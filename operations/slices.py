__author__ = 'Antony Cherepanov'


def different_slices():
    """ Different slice operations. Works for strings, list,... """

    string = "Example"
    print("We have: " + string)
    print("Last element: " + string[-1])
    print("Last element (explicit): " + string[len(string) - 1])
    print("All in the middle: " + string[1:-1])
    print("Start from the second letter: " + string[1:])
    print("Everything but the last: " + string[:6])
    print("Everything but the last (2): " + string[:-1])
    print("Full copy of the string: " + string[:])

different_slices()