#!/usr/bin/python3
"""find intersection of two given arrays using lambda """

intersection = lambda arr1, arr2 : [x for x in arr2 if x in arr1]
print(intersection([1,2,4,54,34,5], [1,3,5,7]))