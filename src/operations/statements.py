__author__ = 'Antony Cherepanov'


def functions_in_if():
    print("\nfunctions_in_if()")

    print("Be careful with calling functions in logical expression at 'if' statement.")
    print("Because of features of boolean logical expressions, not all functions may be called.")

    print("\nif true_func and true_func():")
    if true_func() and true_func():
        print("Both functions were called")

    print("\nif true_func and not false_func():")
    if true_func() and not false_func():
        print("Both functions were called")

    print("\nif false_func() and true_func():")
    if false_func() and true_func():
        print("You will not see this text")
    else:
        print("Only first function was called")

    print("\nif false_func() or true_func():")
    if false_func() or true_func():
        print("Both functions were called")

    print("\nif true_func() or true_func():")
    if true_func() or true_func():
        print("Only first function was called")


def true_func():
    print("it's true!")
    return True


def false_func():
    print("it's false!")
    return False


functions_in_if()