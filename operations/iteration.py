__author__ = 'Antony Cherepanov'


def range_iteration():
    print("\nrange_iteration")

    rng = range(10)
    print("When we call range() functions, we get object tht can iterate: " +
          str(rng))
    print("But it's not an iterator! Let's try:")
    try:
        next(rng)
        print("Wow, iterating!")
    except TypeError:
        print("Nope, not an iterator")

    itr = iter(rng)
    print("To get iterator we should call iter( range_object ): " + str(itr))
    print("Call next( iterator ) to get next value: " + str(next(itr)))
    print("Again: " + str(next(itr)))

    second_itr = iter(rng)
    print("We can create another range iterator: " + str(second_itr))
    print("And it will not depend from previously created iterators: " +
          str(next(second_itr)))

    print("Another way to get next value - call built-in method: " +
          str(itr.__next__))


def single_pass_iterators():
    print("\nsingle_pass_iterators")

    print("Unlike range(), functions like map(), zip() and so on don't " +
          "support multiple active iterators")

    m_obj = map(abs, (-1, 0, 1))
    itr_1 = iter(m_obj)
    itr_2 = iter(m_obj)
    print("We created two map iterators: " + str(itr_1) + " and " + str(itr_2))
    print("Call first iterator: " + str(next(itr_1)))
    print("Call second iterator: " + str(next(itr_2)))
    print("Call first iterator: " + str(next(itr_1)))

    try:
        print("Call second iterator: " + str(next(itr_2)))
    except StopIteration:
        print("End of iteration")

range_iteration()
single_pass_iterators()