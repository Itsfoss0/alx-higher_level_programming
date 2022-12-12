#!/usr/bin/python3
"""convert a given list of tuples to a list of strings using map function"""

colors = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
print(list(map(lambda x : " ".join(x), colors)))

def add_tuple_elements(tup_list, dest):
    for i in range(len(tup_list)):
        for element in tup_list[i]:
            dest.append(element)

    return dest

print(add_tuple_elements(colors, dest=[]))