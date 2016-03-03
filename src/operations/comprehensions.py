__author__ = 'Antony Cherepanov'


def simple_fill_list():
    print("\nsimple_fill_list")

    simple_list = [x for x in range(10)]
    print("We created a list with numbers: " + str(simple_list))


def fill_list_with_filtering():
    print("\nfill_list_with_filtering")

    simple_list = [x for x in range(1, 10) if x % 2 == 0]
    print("We created a list with even numbers: " + str(simple_list))


def nested_loops():
    print("\nnested_loops")

    simple_list = [x ** y for x in range(1, 10) for y in range(1, 3)]
    print("We created a list with numbers and its powered versions: " +
          str(simple_list))


def dict_comprehension():
    print("\ndict_comprehension")

    simple_dict = {x: "hey" for x in range(0, 10, 3)}
    print("We created a dict: " + str(simple_dict))

simple_fill_list()
fill_list_with_filtering()
nested_loops()
dict_comprehension()