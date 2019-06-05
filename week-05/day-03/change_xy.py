# Given a string, compute recursively (no loops) a new string where all the lowercase 'x' chars 
# have been changed to 'y' chars.

def change_xy(str):
    if len(str) == 0: 
        return str
    if str[0] == 'x': 
        return 'y' + change_xy(str[1:])

    return str[0] + change_xy(str[1:])

print(change_xy("xxsdsfefenkefnxx"))
