# Given a string, compute recursively a new string where all the 'x' chars have been removed.

def remove_x(str):
    if len(str) == 0: 
        return str
    if str[0] == 'x': 
        return remove_x(str[1:])

    return str[0] + remove_x(str[1:])

print(remove_x("xxsdsfefenkefnxx"))