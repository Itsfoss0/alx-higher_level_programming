#!/usr/bin/python3
"""Given numbers = range(20), produce a list containing the word "even"
if a number in the numbers is even, and the word "odd" if the number is odd. 
Result would look like "odd","odd", "even"
"""
result = ["even" if x % 2 == 0 else "odd" for x in range(20)]
print(result)