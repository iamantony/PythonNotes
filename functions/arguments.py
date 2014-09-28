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


passing_arguments()