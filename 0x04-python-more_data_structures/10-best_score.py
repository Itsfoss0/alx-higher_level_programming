#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    return max(a_dictionary.keys())


# print(best_score({"John": 33, "Doe": 23}))
