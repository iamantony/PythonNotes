__author__ = 'Antony Cherepanov'


def dir_function():
    """ dir() shows all methods for defined object """
    string = "example"
    print("Show me all methods of string object!\n" + str(dir(string)))


dir_function()