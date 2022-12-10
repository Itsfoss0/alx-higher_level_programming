#!/usr/bin/python3
"""add each elements of two lists together. Use a lambda with two arguments"""

list_1 = ["John", "Doe", "Fugue", "Jordana", "Brewster"]
shows = ["Whiskey Cavalier", "Angie Tribecca", "Brooklyn Nine Nine", "Fringe", "The Sandman"]
print(list(map(lambda x, y : x + " " + y, list_1, shows )))