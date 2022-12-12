#!/usr/bin/python3
"""convert a given list of tuples to a list of strings using map function"""

colors = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
print(list(map(lambda x : "".join(x), colors)))