# Create a method that decrypts the duplicated-chars.txt

def decrypt(file_name):
    list_array=[]
    try:
        with open(file_name,'r') as f:
            content=f.read()
            print(len(content))
            a=list(content)
            for x in a:
                list_array.append(x)
            return list_array
    except IOError:
        print("can't read this file")

def get_ord(return_value_list):
    list2=[]
    for char in return_value:
        a=chr(ord(char)-1)
        list2.append(a)
        str_convert = ''.join(list2)
    return str_convert


return_value = decrypt("duplicated-chars.txt")
print(get_ord("return_value"))

