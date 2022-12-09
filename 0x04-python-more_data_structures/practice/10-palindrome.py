#!/usr/bin/python3
"""find palindromes in a given list of strings"""
palindromes = lambda str_list : [ string for string in str_list if string == string[::-1]]

print(palindromes(["John", "Doe", "Dad", "Java", "dad", "bob"]))