__author__ = 'Antony Cherepanov'


def repeat_string():
    """ Repeat string several times simply multiplying it by some number """
    string = "And Again "
    long_string = string * 5
    print("Original string :", string)
    print("Repeated string :", long_string)


def immutability():
    """ Strings are immutable objects. You can't change them. """
    string = "example"
    print("Our string: " + string + "; id = " + str(id(string)))

    try:
        string[0] = 'f'
        print("You will not see this because of exception!")
    except Exception:
        print("Failed to change string object!")

    string = "new " + string
    print("We can change string only by creating new object: " + string + "; id = " + str(id(string)))


def transform_to_list():
    """ Transform string to list of it's characters """

    string = "example"
    characters_list = list(string)
    print("Transform string \"" + string + "\" to list: " + str(characters_list))


def string_formatting():
    string_one = "Example"
    string_two = "string formatting"

    print("%s of %s 1" % (string_one, string_two))
    print("{0} of {1} 2".format(string_one, string_two))
    print("{} of {} 3".format(string_one, string_two))


def string_formatting_with_dict():
    data = dict(name="Bob", action="working")
    formatted_string_first = "1: %(name)s is %(action)s"
    print(formatted_string_first % data)

    formatted_string_second = "2: {name} is {action}"
    print(formatted_string_second.format(name="Ann", action="cooking"))

    from string import Template
    temp = Template("3: $name is $action")
    print(temp.substitute(name="Jane", action="reading"))


repeat_string()
immutability()
transform_to_list()
string_formatting()
string_formatting_with_dict()