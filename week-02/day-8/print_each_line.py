# Write a program that opens a file called "my-file.txt", then prints
# each line from the file.
# If the program is unable to read the file (for example it does not exist),
# then it should print the following error message: "Unable to read file: my-file.txt"

f=open("my_file.txt","w")
f.write("Hello\nWorld")
f.close()

try:
    f=open("my-file.txt")
    content=f.readlines()
    print(content)
except IOError:
    print("Unable to read file:my-file.txt")
finally:
    print("completed")