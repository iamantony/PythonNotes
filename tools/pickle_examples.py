__author__ = 'Antony Cherepanov'

import pickle
import os


def save_dict_to_file():
    print("\nsave_dict_to_file()")

    simple_dict = {"key1": 224, "kkl": "strong"}
    print("Our dict: " + str(simple_dict))
    print("Let's serialise it and save to file")

    test_file = open("datafile.pkl", "wb")
    pickle.dump(simple_dict, test_file)
    test_file.close()

    print("And now recreate it from file!")
    reopened_test_file = open("datafile.pkl", "rb")
    recreated_dict = pickle.load(reopened_test_file)
    reopened_test_file.close()
    print("Recreated dict: " + str(recreated_dict))
    print("Are they the same: " + str(simple_dict == recreated_dict))

    os.remove("datafile.pkl")


save_dict_to_file()