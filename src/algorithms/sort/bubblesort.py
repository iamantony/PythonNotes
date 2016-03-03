__author__ = 'Antony Cherepanov'


def bubble_sort(t_input):
    """ Bubble Sort Algorithm
    Simple and slow algorithm
    http://en.wikipedia.org/wiki/Bubble_sort

    Best case performance: O(n^2)
    Worst case performance: O(n^2)
    Worst Case Auxiliary Space Complexity: O(1)

    :param t_input: [list] of numbers
    :return: [list] - sorted list of numbers
    """

    array = t_input[:]
    while True:
        swapped = False
        for i in range(len(t_input) - 1):
            if array[i + 1] < array[i]:
                # swap elements
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        if swapped is False:
            break

    return array
