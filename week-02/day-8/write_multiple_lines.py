# Create a function that takes 3 parameters: a path, a word and a number
# and is able to write into a file.
# The path parameter should be a string that describes the location of the file you wish 
# to modify
# The word parameter should also be a string that will be written to the file as individual 
# The number parameter should describe how many lines the file should have.
# If the word is "apple" and the number is 5, it should write 5 lines
# into the file and each line should read "apple"
# The function should not raise any errors if it could not write the file.

def write_multiple_lines(path,word,number):
    f=open(path,'w')
    try:
        for i in range(number):
            f.write(word+'\n')
        f.close()

    except IOError:
        print("can't write the file")
        
    finally:
        ("completed")
write_multiple_lines(r"C:\Users\Angela_Shi\Desktop\angela\week2\day8\multiple_lines.txt","apple",5)

