__author__ = 'Antony Cherepanov'

from random import randint
import sys

sys.setrecursionlimit(10000)


class PivotPosition(object):
    """ List of names of rules to choose pivot position """
    FIRST, LAST, MEDIAN, RANDOM = range(0, 4)


def quick_sort(t_input, t_pivot_position=PivotPosition.RANDOM):
    """ Quick sort algorithm.
    No extra memory needed.
    @input:
    - t_input - list of numbers
    - t_pivotPosition - desired rule of choosing pivot's position
    @output:
    - list(1,2, ...) - sorted list of elements (same input object)
    """

    array = t_input[:]
    sort(array, 0, len(t_input) - 1, t_pivot_position)
    return array


def sort(t_input, t_left, t_right, t_pivot_position):
    """ Real Quick Sort procedure
    @input:
    - t_input - input array of numbers
    - t_left - index of left boundary of inspecting array (included)
    - t_right - index of right boundary of inspecting array (included)
    - t_pivotPosition - desired rule of choosing pivot's position
    """

    i = t_left
    j = t_right
    pivot_index = choose_pivot(t_left, t_right, t_pivot_position)
    pivot_value = t_input[pivot_index]

    while True:
        while t_input[i] < pivot_value:
            i += 1
        while pivot_value < t_input[j]:
            j -= 1

        if i <= j:
            if t_input[i] > t_input[j]:
                t_input[i], t_input[j] = t_input[j], t_input[i]
            i += 1
            j -= 1

        if i > j:
            break

    if i < t_right:
        sort(t_input, i, t_right, t_pivot_position)
    if t_left < j:
        sort(t_input, t_left, j, t_pivot_position)


def choose_pivot(t_left, t_right, t_pivot_position):
    """ Choose index of pivot element
    @input:
    - t_left - index of left boundary of inspecting array (included)
    - t_right - index of right boundary of inspecting array (included)
    - t_pivotPosition - desired rule of choosing pivot's position
    @output:
    - int - chosen index of pivot element
    """

    if t_right <= t_left:
        return t_left

    if t_pivot_position == PivotPosition.FIRST:
        return t_left
    elif t_pivot_position == PivotPosition.LAST:
        return t_right
    elif t_pivot_position == PivotPosition.MEDIAN:
        return (t_right + t_left) // 2
    elif t_pivot_position == PivotPosition.RANDOM:
        return randint(t_left, t_right)
    else:
        print("ChoosePivot(): Warning - invalid rule! Choose first element")
        return t_left