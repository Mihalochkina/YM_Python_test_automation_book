# Regular Expressions
# Define if a string contains the required characters. E.g. if '7865serS3' includes '583' - True; '973' - False

import re

string = input("Enter a string here: ")
req_characters = input("Enter the required characters here: ")

def check_required_characters(req_characters, string):
    for char in req_characters:
        if re.search(re.escape(char), string):
            pass
        else:
            return False
    return True


if check_required_characters(req_characters, string) is True:
    print (f"The string {string} contains {req_characters}")
else:
    print(f"The string {string} doesn't contain {req_characters}")






