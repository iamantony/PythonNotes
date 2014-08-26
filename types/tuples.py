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



ways_to_create()
immutability()
