__author__ = 'Antony Cherepanov'


def immutable_set():
    print("\nimmutable_set():")
    simple_list = [1, 2, 1, 5, 4, 7, 7]
    simple_set = set(simple_list)

    print("List :" + str(simple_list))
    print("Set that based on this list :" + str(simple_set))

    print("Check that sets are immutable:")
    try:
        simple_set.add([0])
        print("Will not print")
    except Exception:
        print("Immutable!")


def set_operations():
    print("\nset_operations():")
    first = {1, 4, 7, 9}
    print("First set: " + str(first))
    second = {1, 3, 4, 10}
    print("Second set: " + str(second))

    print("Difference: " + str(first - second))
    print("Union: " + str(first | second))
    print("Intersection: " + str(first & second))
    print("Symmetric Difference (XOR): " + str(first ^ second))


def list_in_set():
    print("\nlist_in_set():")
    simple = set([1, 4, 7, 9])
    print("Set could be created on base of list: " + str(simple))

    print("But we can't add list to set because lists are mutable.")
    try:
        simple.add([10, 9])
        print("Will not print")
    except Exception:
        print("Failed to add list to set")

    print("Workaround: we can add frozensets to set because they are immutable!")
    simple.add(frozenset([6, 7]))
    print("Set with frozenset inside: " + str(simple))


immutable_set()
set_operations()
list_in_set()