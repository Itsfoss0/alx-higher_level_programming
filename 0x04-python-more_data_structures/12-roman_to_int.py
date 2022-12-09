#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not len(roman_string):
        return 0

    result = 0

    for ch in roman_string:
        if ch == 'I':
            result += 1
        elif ch == 'V':
            result += 5
        elif ch == 'X':
            result += 10
        elif ch == 'L':
            result += 50
        elif ch == 'C':
            result += 100
        elif ch == 'D':
            result += 500
        elif ch == 'M':
            result += 1000

    return result
