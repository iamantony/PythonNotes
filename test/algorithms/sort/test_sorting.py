__author__ = 'Antony Cherepanov'

import unittest
import os
from src.Algorithms.Sort import mergesort, insertionsort, selectionsort, \
    bubblesort, gnomesort, quicksort

ARR_10 = None
ARR_100 = None
ARR_1000 = None
ARR_10000 = None


def create_numbers_array():
    """ Create test arrays with numbers
    :return: [boolean] - True if all arrays were created, otherwise False
    """

    global ARR_10, ARR_100, ARR_1000, ARR_10000
    script_folder = os.path.dirname(os.path.abspath(__file__)) + str(os.sep)
    ARR_10 = numbers_from_file(script_folder + "10.txt")
    ARR_100 = numbers_from_file(script_folder + "100.txt")
    ARR_1000 = numbers_from_file(script_folder + "1000.txt")
    ARR_10000 = numbers_from_file(script_folder + "10000.txt")

    if ARR_10 is None or ARR_100 is None or \
            ARR_1000 is None or ARR_10000 is None:
        return False

    return True


def numbers_from_file(path):
    """ Read file with numbers and save them to list
    :param path: [string] - path to file with test numbers
    :return: [list] numbers from file or [None] if failed to read file
    """

    result = list()
    try:
        for line in open(path):
            result.append(int(line))
    except OSError:
        print("Failed to create array")
        return None

    return result


def is_sorted(array):
    """ Check if array of numbers is sorted
    :param array: [list] of numbers
    :return: [boolean] - True if array is sorted and False otherwise
    """

    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False

    return True


class MergeSortTest(unittest.TestCase):
    def test_10(self):
        global ARR_10
        result = mergesort.merge_sort(ARR_10)
        self.assertTrue(is_sorted(result))

    def test_100(self):
        global ARR_100
        result = mergesort.merge_sort(ARR_100)
        self.assertTrue(is_sorted(result))

    def test_1000(self):
        global ARR_1000
        result = mergesort.merge_sort(ARR_1000)
        self.assertTrue(is_sorted(result))

    def test_10000(self):
        global ARR_10000
        result = mergesort.merge_sort(ARR_10000)
        self.assertTrue(is_sorted(result))


class InsertionSortTest(unittest.TestCase):
    def test_10(self):
        global ARR_10
        result = insertionsort.insertion_sort(ARR_10)
        self.assertTrue(is_sorted(result))

    def test_100(self):
        global ARR_100
        result = insertionsort.insertion_sort(ARR_100)
        self.assertTrue(is_sorted(result))

    def test_1000(self):
        global ARR_1000
        result = insertionsort.insertion_sort(ARR_1000)
        self.assertTrue(is_sorted(result))

    def test_10000(self):
        global ARR_10000
        result = insertionsort.insertion_sort(ARR_10000)
        self.assertTrue(is_sorted(result))


class SelectionSortTest(unittest.TestCase):
    def test_10(self):
        global ARR_10
        result = selectionsort.selection_sort(ARR_10)
        self.assertTrue(is_sorted(result))

    def test_100(self):
        global ARR_100
        result = selectionsort.selection_sort(ARR_100)
        self.assertTrue(is_sorted(result))

    def test_1000(self):
        global ARR_1000
        result = selectionsort.selection_sort(ARR_1000)
        self.assertTrue(is_sorted(result))

    def test_10000(self):
        global ARR_10000
        result = selectionsort.selection_sort(ARR_10000)
        self.assertTrue(is_sorted(result))


class BubbleSortTest(unittest.TestCase):
    def test_10(self):
        global ARR_10
        result = bubblesort.bubble_sort(ARR_10)
        self.assertTrue(is_sorted(result))

    def test_100(self):
        global ARR_100
        result = bubblesort.bubble_sort(ARR_100)
        self.assertTrue(is_sorted(result))

    def test_1000(self):
        global ARR_1000
        result = bubblesort.bubble_sort(ARR_1000)
        self.assertTrue(is_sorted(result))

    def test_10000(self):
        global ARR_10000
        result = bubblesort.bubble_sort(ARR_10000)
        self.assertTrue(is_sorted(result))


class GnomeSortTest(unittest.TestCase):
    def test_10(self):
        global ARR_10
        result = gnomesort.gnome_sort(ARR_10)
        self.assertTrue(is_sorted(result))

    def test_100(self):
        global ARR_100
        result = gnomesort.gnome_sort(ARR_100)
        self.assertTrue(is_sorted(result))

    def test_1000(self):
        global ARR_1000
        result = gnomesort.gnome_sort(ARR_1000)
        self.assertTrue(is_sorted(result))

    # Too long
    # def test_10000(self):
    #     global ARR_10000
    #     result = gnomesort.gnome_sort(ARR_10000)
    #     self.assertTrue(is_sorted(result))


class QuickSortTest(unittest.TestCase):
    def test_first_elem_10(self):
        global ARR_10
        result = quicksort.quick_sort(ARR_10, quicksort.PivotPosition.FIRST)
        self.assertTrue(is_sorted(result))

    def test_first_elem_100(self):
        global ARR_100
        result = quicksort.quick_sort(ARR_100, quicksort.PivotPosition.FIRST)
        self.assertTrue(is_sorted(result))

    def test_first_elem_1000(self):
        global ARR_1000
        result = quicksort.quick_sort(ARR_1000, quicksort.PivotPosition.FIRST)
        self.assertTrue(is_sorted(result))

    def test_first_elem_10000(self):
        global ARR_10000
        result = quicksort.quick_sort(ARR_10000, quicksort.PivotPosition.FIRST)
        self.assertTrue(is_sorted(result))

    def test_last_elem_10(self):
        global ARR_10
        result = quicksort.quick_sort(ARR_10, quicksort.PivotPosition.LAST)
        self.assertTrue(is_sorted(result))

    def test_last_elem_100(self):
        global ARR_100
        result = quicksort.quick_sort(ARR_100, quicksort.PivotPosition.LAST)
        self.assertTrue(is_sorted(result))

    def test_last_elem_1000(self):
        global ARR_1000
        result = quicksort.quick_sort(ARR_1000, quicksort.PivotPosition.LAST)
        self.assertTrue(is_sorted(result))

    def test_last_elem_10000(self):
        global ARR_10000
        result = quicksort.quick_sort(ARR_10000, quicksort.PivotPosition.LAST)
        self.assertTrue(is_sorted(result))

    def test_median_elem_10(self):
        global ARR_10
        result = quicksort.quick_sort(ARR_10, quicksort.PivotPosition.MEDIAN)
        self.assertTrue(is_sorted(result))

    def test_median_elem_100(self):
        global ARR_100
        result = quicksort.quick_sort(ARR_100, quicksort.PivotPosition.MEDIAN)
        self.assertTrue(is_sorted(result))

    def test_median_elem_1000(self):
        global ARR_1000
        result = quicksort.quick_sort(ARR_1000, quicksort.PivotPosition.MEDIAN)
        self.assertTrue(is_sorted(result))

    def test_median_elem_10000(self):
        global ARR_10000
        result = quicksort.quick_sort(ARR_10000, quicksort.PivotPosition.MEDIAN)
        self.assertTrue(is_sorted(result))

    def test_rand_elem_10(self):
        global ARR_10
        result = quicksort.quick_sort(ARR_10, quicksort.PivotPosition.RANDOM)
        self.assertTrue(is_sorted(result))

    def test_rand_elem_100(self):
        global ARR_100
        result = quicksort.quick_sort(ARR_100, quicksort.PivotPosition.RANDOM)
        self.assertTrue(is_sorted(result))

    def test_rand_elem_1000(self):
        global ARR_1000
        result = quicksort.quick_sort(ARR_1000, quicksort.PivotPosition.RANDOM)
        self.assertTrue(is_sorted(result))

    def test_rand_elem_10000(self):
        global ARR_10000
        result = quicksort.quick_sort(ARR_10000, quicksort.PivotPosition.RANDOM)
        self.assertTrue(is_sorted(result))


create_numbers_array()
if __name__ == "__main__":
    unittest.main()