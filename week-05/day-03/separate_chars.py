# Given a string, compute recursively a new string where all the adjacent chars are now separated by a *


def separate_chars(str):
    if len(str) == 0: 
        return str
    if str[0]: 
        return str[0] + '*' + separate_chars(str[1:])

print(separate_chars("xxsdsfefenkefnxx"))