#!/usr/bin/python3
"""Find all of the numbers from 1-1000 that are divisible by 7"""
divisible = [num for num in range(1,1001) if num % 7 == 0]
print(divisible)