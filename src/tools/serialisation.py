__author__ = 'Antony Cherepanov'

import pickle
import json
import os


def save_dict_to_file_via_pickle():
    print("\nsave_dict_to_file_via_pickle()")

    simple_dict = {"key1": 224, "kkl": "strong"}
    print("Our dict: " + str(simple_dict))
    print("Let's serialise it and save to file")

    test_file = open("datafile.pkl", "wb")
    pickle.dump(simple_dict, test_file)
    test_file.close()

    print("Let's see what inside: " + str(open("datafile.pkl", "rb").read()))

    print("And now recreate it from file!")
    reopened_test_file = open("datafile.pkl", "rb")
    recreated_dict = pickle.load(reopened_test_file)
    reopened_test_file.close()
    print("Recreated dict: " + str(recreated_dict))
    print("Are they the same: " + str(simple_dict == recreated_dict))

    os.remove("datafile.pkl")


def save_dict_as_json():
    print("\nsave_dict_as_json()")

    simple_dict = {"key1": 224, "kkl": "strong"}
    print("Our dict: " + str(simple_dict))
    print("Let's serialise it and save to json file")

    json.dump(simple_dict, fp=open("testjson.txt", "w"))

    print("Let's see what inside: " + open("testjson.txt").read())

    recreated_dict = json.load(open("testjson.txt"))
    print("Recreated dict: " + str(recreated_dict))

    os.remove("testjson.txt")


save_dict_to_file_via_pickle()
save_dict_as_json()