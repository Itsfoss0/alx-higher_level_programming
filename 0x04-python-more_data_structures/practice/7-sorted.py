#!/usr/bin/python3
"""rearrange positive and negative numbers in a given array"""
rearranged = lambda array : sorted(array, reverse=True)

print(rearranged([-1, -3, -7, 4, 5, 9, 2]))