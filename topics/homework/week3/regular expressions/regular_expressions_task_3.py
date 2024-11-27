# Regular Expressions
# Define if the string contains at least one Upper case letter followed by Lower case letters. E.g. '75serS3' - False; '75WseTrS3' - True;

import re

string = input("Enter a string here: ")

def check_uppercase_followed_by_lowercase(string):
    pattern = r'[A-Z][a-z]+'
    match = re.search(pattern, string)
    return match is not None


# Check if the string contains an uppercase letter followed by lowercase letters
if check_uppercase_followed_by_lowercase(string) is True:
    print (f"The string contains at least one Upper case letter followed by Lower case letters")
else:
    print(f"The string doesn't contain at least one Upper case letter followed by Lower case letters")