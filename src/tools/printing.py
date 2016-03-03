__author__ = 'Antony Cherepanov'

import os
import sys


def different_ways_to_print():
    print("\ndifferent_ways_to_print()")

    a, b, c = 42, "i'm a string", [99, 0.2]
    print("The standard way:")
    print(a, b, c)

    print("With special separator:")
    print(a, b, c, sep=" -- ")

    print("With special line ending:")
    print(a, b, c, end=" -it's-the-end-of-the-line-")

    print("Print to file:")
    print(a, b, c, file=open("test.txt", "w"))
    print("From file: " + open("test.txt").read())

    os.remove("test.txt")


def print_object_info():
    print("\nprint_object_info()")
    print("Sometimes we want to know with what object we are working.")
    print("For that purpose we can use function id().")
    print("It return address of the object. Example: ")
    print(id("string"))
    print("To convert address to hex number use hex()")
    simple_list = [1, 2]
    print(str(simple_list) + " = " + hex(id(simple_list)))


def stdout_redirection():
    print("\nstdout_redirection()")

    print("After this line all print output will be redirected to file")
    temp = sys.stdout
    sys.stdout = open("log.txt", "a")
    print("This string will be saved to file!")
    sys.stdout.close()
    sys.stdout = temp

    print("Back! Let's see what in a file:")
    print(open("log.txt").read())

    os.remove("log.txt")


different_ways_to_print()
print_object_info()
stdout_redirection()