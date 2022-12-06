#!/usr/bin/python3
"""Get the index and the value as a tuple for items in the list 
“hi”, 4, 8.99, 'apple', ('t,b','n'). Result would look like (index, value), (index, value)
"""

data = ['hi', 4, 8.99, 'apple', ('t','b','n')]
data_list = [(data.index(x), x) for x in data]
print(data_list)