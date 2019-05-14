# Write a function that copies the contents of a file into another
# It should take the filenames as parameters
# It should return a boolean that shows if the copy was successful
import shutil

def copy_file(oldfile,newfile):
    shutil.copyfile(oldfile,newfile)
    f=open(oldfile,'r')
    f.seek(0)
    text1 = f.read()
    print(text1)

    f=open(newfile,'r')
    f.seek(0)
    text2 = f.read()
    print(text2)

    if text1 == text2:
        return True
    else:
        return False

print(copy_file("my_file.txt","my-file.txt"))