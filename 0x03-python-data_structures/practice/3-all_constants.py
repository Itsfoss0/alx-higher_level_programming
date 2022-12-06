#!/usr/bin/python3
"""Create a list of all the consonants in the string 
'Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams' """

vowels = "aeiou"
string = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
consonants = [letter for letter in string if not letter in vowels and letter != " "]
print(consonants)


