__author__ = 'Antony Cherepanov'


def ways_to_create():
    print("\nways_to_create()")

    # On the end - comma!
    first = "first value",
    print("1: ", str(first))

    # Also we can create tuple via tuple()
    second = ("second value", 2)
    print("2: ", str(second))

    nested = (1, (2, 3))
    print("3 nested: ", str(nested))


def immutability():
    print("\nimmutability()")

    simple_tuple = 1, 2, 3
    print("tuple = ", str(simple_tuple))

    try:
        simple_tuple[0] = 10
        print("This will not be printed")
    except:
        print("We can't change value in tuple. But we can recreate them!")

    simple_list = [1, 4, 99]
    second_tuple = simple_tuple, simple_list
    print("Modified tuple: " + str(second_tuple))

    simple_list[0] = 191
    print("After list modification: " + str(second_tuple))


def assignment():
    print("\nassignment()")

    print("Assign string to variables in tuple:")
    (a, b, c) = "ABC"
    print(a, b)


def extended_sequence_unpacking():
    print("\nextended_sequence_unpacking()")

    simple_list = [1, 2, 3, 4, 5]
    print("We have some object (string, list, tuple, set): " + str(simple_list))
    print("Suppose, we want only first and the last element of this object.")
    print("And we don't know the length of it.")
    print("We can use Extended Sequence unpacking:")
    first, *middle, last = simple_list
    print("First = " + str(first))
    print("Last = " + str(last))
    print("Middle = " + str(middle))


ways_to_create()
immutability()
assignment()
extended_sequence_unpacking()