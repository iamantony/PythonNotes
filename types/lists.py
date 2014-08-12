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


def extending():
    """ Several ways to extend list  """

    some_list = list((1, 2))
    print("At the start: " + str(some_list))

    some_list[:0] = [-1, 0]
    print("Prepend values [:0]: " + str(some_list))

    some_list[len(some_list):] = [3, 4]
    print("Append values [len(some_list):]: " + str(some_list))

    some_list.extend([5, 6])
    print("Explicit extending: " + str(some_list))


def sorting():
    """ Sorting options """

    some_list = [2, 5, 1, -1, -10, 9]
    print("Our list: " + str(some_list))

    some_list.sort()
    print("Standart sorting: " + str(some_list))

    some_list.sort(key=abs)
    print("Sorting by absolute values: " + str(some_list))


nesting()
extending()
sorting()