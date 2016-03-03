__author__ = 'Antony Cherepanov'


def gnome_sort(t_input):
    """ Gnome Sort Algorithm
    Simple and slow algorithm
    http://en.wikipedia.org/wiki/Gnome_sort

    Best case performance: O(n^2)
    Worst case performance: O(n)
    Worst Case Auxiliary Space Complexity: O(1)

    :param t_input: [list] of numbers
    :return: [list] - sorted list of numbers
    """

    array = t_input[:]
    current_pos = 0
    saved_pos = 0
    while current_pos < len(t_input) - 1:
        if array[current_pos] <= array[current_pos + 1]:
            # check if we can jump further to the previously saved position
            if saved_pos != 0:
                current_pos = saved_pos
                saved_pos = 0
            current_pos += 1
        else:
            # swap elements
            array[current_pos], array[current_pos + 1] = \
                array[current_pos + 1], array[current_pos]
            # check position
            if 0 < current_pos:
                # if we are not at the start, then save this position
                # and step back
                if saved_pos is 0:
                    saved_pos = current_pos
                current_pos -= 1
            else:
                # if we are at the beginning - go to the next position
                current_pos += 1

    return array
