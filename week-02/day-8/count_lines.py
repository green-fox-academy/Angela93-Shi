# Write a function that takes a filename as string,
# then returns the number of lines the file contains.
# It should return zero if it can't open the file, and
# should not raise any error.

def count_lines(file):
    try:
        f = open(file)
        content = f.readlines()
        return len(content)

    except:IOError
    return 0

print(count_lines("my_file.txt"))
