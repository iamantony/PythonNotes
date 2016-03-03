__author__ = 'Antony Cherepanov'


def selection_sort(t_input):
    """ Selection Sort Algorithm
    Simple, stable algorithm with in-place sorting
    http://en.wikipedia.org/wiki/Selection_sort

    Best case performance: O(n^2)
    Worst case performance: O(n^2)
    Worst Case Auxiliary Space Complexity: O(n)

    :param t_input: [list] of numbers
    :return: [list] - sorted list of numbers
    """

    array = t_input[:]
    for i in range(len(t_input) - 1):
        min_element_index = i
        for j in range(i + 1, len(t_input)):
            if array[j] < array[min_element_index]:
                min_element_index = j

        if i != min_element_index:
            # swap current element with found min element
            array[i], array[min_element_index] = \
                array[min_element_index], array[i]

    return array
