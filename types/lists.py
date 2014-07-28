__author__ = 'Antony Cherepanov'


def nesting():
    """ List can hold another list! """

    matrix = list()
    # First row
    matrix.append([1, 2, 3])
    # Second
    matrix.append([4, 5, 6])
    # Third
    matrix.append([7, 8, 9])

    print("Our matrix as list of lists: " + str(matrix))
    print("Second element of third row: " + str(matrix[2][1]))


nesting()