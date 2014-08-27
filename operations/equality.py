__author__ = 'Antony Cherepanov'


def diff_ways_to_equality_check():
    print("\ndiff_ways_to_equality_check()")

    l1 = l2 = [1, 2, 3]
    print("Our lists: " + str(l1) + ", " + str(l2) + ". They reference to the same object")
    print("l1 == l2 ? : ", l1 == l2)
    print("l1 is l2 ? : ", l1 is l2)

    l3 = [1, 2]
    l4 = [1, 2]
    print("Our lists: " + str(l3) + ", " + str(l4) + ". They reference to different objects")
    print("l3 == l4 ? : ", l3 == l4)
    print("l3 is l4 ? : ", l3 is l4)


diff_ways_to_equality_check()