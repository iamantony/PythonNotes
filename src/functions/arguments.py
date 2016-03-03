__author__ = 'Antony Cherepanov'


def passing_arguments():
    print("\npassing_arguments()")

    print("Immutable arguments are effectively passed 'by value'")
    print("So inside a function we work with copy of variable and")
    print("any changed made inside the function will not affect")
    print("original variable.")

    example_str = "hey there"
    print("Example: string = " + example_str)
    print("Object: " + str(id(example_str)))

    def get_immutable(arg_str):
        arg_str = "jjj"
        print("Inside function we changed string: " + arg_str)
        print("Object: " + str(id(arg_str)))

    get_immutable(example_str)
    print("But outside of the function our string still have the same value: " +
          example_str)

    print("____")
    print("Mutable arguments are effectively passed 'by pointer'")
    print("Such variables can be changed inside functions")

    example_list = [1, 2, 3]
    print("Example: list = " + str(example_list))
    print("Object: " + str(id(example_list)))

    def get_mutable(arg_list):
        arg_list[0] = "wow"
        print("Inside function we changed list: " + str(arg_list))
        print("Object: " + str(id(arg_list)))

    get_mutable(example_list)
    print("Now we outside and we have changed modified list: " +
          str(example_list))


def positional_arguments():
    print("\npositional_arguments()")

    print("It's a normal case. Passed argument values match to argument names")
    print("in a function header by position, from left to right")

    def func(a, b, c):
        print(a, b, c)

    func(1, 2, 3)


def keyword_arguments():
    print("\nkeyword_arguments()")

    print("Keyword arguments allow us to match values by name of argument.")
    print("In this case position of values doesn't matter")

    def func(a, b, c):
        print(a, b, c)

    func(c=3, a=1, b=2)


def default_arguments():
    print("\ndefault_arguments()")

    print("We can declare default values for function arguments. In this case")
    print("if we don't pass a value to argument, " +
          "it's default value will be used")

    def func(a=1, b=2, c=3):
        print(a, b, c)

    print("Call function without argument values")
    func()

    print("Call function with several argument values")
    func(c=10)

    print("Call function with all values")
    print(0, 0, 0)

    print()
    print("Beware mutable defaults: if you code a default to be a mutable")
    print("object (list for example), the same single mutable object will be")
    print("reused every time the function is later called!")

    def func_with_mutable(val=list()):
        val.append(1)
        print(val)

    func_with_mutable()
    func_with_mutable()
    func_with_mutable()


def arbitrary_arguments():
    print("\narbitrary_arguments()")

    print("Functions can use special arguments preceded with")
    print("one or two * characters to collect an arbitrary number")
    print("of possibly extra arguments")
    print("All positional arguments will be added to argument with one *")
    print("All keyword arguments will be added to argument with two *")

    def func(*pargs, **kargs):
        print(pargs, kargs)

    func()
    func(1, 2)
    func(my_key=False)
    func(1, 2, 3, a='this is a string', b=True)


def combination_of_arguments():
    print("\ncombination_of_arguments()")

    print("If you choose to use and combine the special argument-matching")
    print("modes, Python will ask you to follow these ordering rules among")
    print("the modes’ optional components:")

    print("In a function header:")
    print("any normal arguments (name); followed by any default arguments")
    print("(name=value); followed by the *name form; followed by any name")
    print("or name=value keyword-only arguments; followed by the **name form")

    print()
    print("In a function call:")
    print("any positional arguments (value); followed by a combination")
    print("of any keyword arguments (name=value) and the *iterable form;")
    print("followed by the **dict form")
    print()

    def func(a, b, c=42, *pargs, keyword='test', **kargs):
        print(a, b, c, pargs, keyword, kargs)

    func(1, 2, 41, 1, 1, 1, keyword='call_func', my_arbitrary_key="this")


def unpacking_arguments():
    print("\nunpacking_arguments()")

    print("We can use the * syntax when we call a function. In this context")
    print("it will unpacks a collection of arguments")

    def func(a, b, c, d):
        print(a, b, c, d)

    list_args = [1, 2, 3, 4]
    print("We can unpack list: " + str(list_args))
    func(*list_args)

    dict_args = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    print("We can unpack dict: " + str(dict_args))
    func(**dict_args)

    print("We can combine objects unpacking:")
    func(*(1, 2), **{'d': 4, 'c': 3})
    func(1, *(2, 3), d=4)
    func(1, *(2,), c=3, **{'d': 4})


passing_arguments()
positional_arguments()
keyword_arguments()
default_arguments()
arbitrary_arguments()
combination_of_arguments()
unpacking_arguments()