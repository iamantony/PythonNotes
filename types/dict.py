__author__ = 'Antony Cherepanov'


def get_list_of_items():
    print("\nget_list_of_items():")
    some_dict = dict(test=1, some_list=[1, 2, 3], useful="This is a dict!")
    print("Dict: " + str(some_dict))
    print("Dict keys: " + str(some_dict.keys()))
    print("Dict values: " + str(some_dict.values()))
    print("Dict items: " + str(some_dict.items()))


def mutability_example():
    print("\nmutability_example():")
    some_list = [1, 4, 9, 99]
    some_dict = dict([("test", 1), ("list", some_list), ("useful","This is a dict!" )])
    print("External list: " + str(some_list))
    print("Dict with list as value: " + str(some_dict))

    some_list.append(9567)
    print("List changed outside: " + str(some_list))
    print("Dict also changed: " + str(some_dict))


def sort_dict():
    print("\nsort_dict():")
    some_dict = {'a': 1, 'c': 56, 'z': 2}
    print("Dict: " + str(some_dict))
    for key in sorted(some_dict):
        print(str(key) + ": " + str(some_dict[key]))


get_list_of_items()
mutability_example()
sort_dict()