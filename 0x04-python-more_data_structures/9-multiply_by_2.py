#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return ({key: (a_dictionary[key] * 2) for key in a_dictionary})
# print(multiply_by_2({"John": 22, "Doe": 55}))
