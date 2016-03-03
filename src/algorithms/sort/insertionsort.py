__author__ = 'Antony Cherepanov'


def insertion_sort(t_input):
    """ Insertion Sort Algorithm
    Simple, stable algorithm with in-place sorting
    http://en.wikipedia.org/wiki/Insertion_sort

    Best case performance: O(n) - when array is already sorted
    Worst case performance: O(n^2) - when array sorted in reverse order
    Worst Case Auxiliary Space Complexity: O(n)

    :param t_input: [list] of numbers
    :return: [list] - sorted list of numbers
    """

    # copy input to array that will be sorted
    array = t_input[:]

    for i in range(1, len(t_input)):
        j = i
        while 0 < j and array[j] < array[j - 1]:
            # swap elements
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1

    return array