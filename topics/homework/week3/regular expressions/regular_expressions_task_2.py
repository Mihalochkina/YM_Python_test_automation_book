# Regular Expressions
# Count a number of Upper case letters in the string. E.g. '7865serS3' - 'Number of Capital letters: 1'

import re

string = input("Enter a string here: ")

def count_uppercase_letters(string):
    uppercase_letters = re.findall(r'[A-Z]', string)
    return len(uppercase_letters)


# Count the number of uppercase letters in the string
uppercase_count = count_uppercase_letters(string)
print("Number of Capital letters:", uppercase_count)
