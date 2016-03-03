__author__ = 'Antony Cherepanov'


def while_with_else():
    print("\nwhile_with_else")

    print("If inside while() loop 'break' was not called, code under the 'else' will be executed")

    print("\nLoop without break:")
    i = 2
    while i < 5:
        print("Inside loop")
        i += 1
    else:
        print("Code inside else")

    print("End of loop")

    print("\nLoop with break:")
    i = 2
    while i < 5:
        print("Inside loop")
        if i == 3:
            print("Break!")
            break

        i += 1
    else:
        print("Code inside else")

    print("End of loop")


def for_with_else():
    print("\nfor_with_else")

    print("If inside for() loop 'break' was not called, code under the 'else' will be executed")

    print("\nLoop without break")
    for i in range(3):
        print("Inside loop")
    else:
        print("This is else")

    print("End of loop")


def iterate_through_object():
    print("\niterate_through_object")

    print("\nIterate simple list:")
    simple_list = [1, 2, 3, 4]
    for i in simple_list:
        print("List element: " + str(i))

    print("\nIterate dict:")
    simple_dict = {1: "1", 2:"2", 3: "3"}
    for i in simple_dict:
        print("Key: " + str(i) + "; Value: " + simple_dict[i])

    for (key, value) in simple_dict.items():
        print(str(key) + " => " + value)

    print("\nIterate list of tuples:")
    list_of_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    for (a, b, c) in list_of_tuples:
        print(a, b, c)

    print("\n With extended sequence assignment")
    for (*a, b) in list_of_tuples:
        print(a, b)


def parallel_traversals():
    print("\nparallel_traversals")

    first = [1, 2, 3, 4]
    second = [5, 6, 7, 8]
    msg = "What if we want to iterate two objects (in our case lists) " + \
        "of the same number of elements at the same time? We can you zip:"
    print(msg)

    for (x, y) in zip(first, second):
        print(x, y)

    print("\nBut what if objects have different number of elements?")
    print("zip() function will truncate result sequence to the length " +
          "of the shortest")

    first.append(42)
    print("First list now have one more element: " + str(first))
    for (x, y) in zip(first, second):
        print(x, y)


while_with_else()
for_with_else()
iterate_through_object()
parallel_traversals()