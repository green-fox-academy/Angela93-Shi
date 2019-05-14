# Read all data from 'log.txt'.
# Each line represents a log message from a web server
# Write a function that returns an array with the unique IP adresses.
# Write a function that returns the GET / POST request ratio.
import re
def logs():
    f=open("log.txt")
    datas=f.readlines()
    print(type(datas))
    for data in datas:
        print(data)
        data=f.readlines()
    return datas
    f.close()

def array_get(list):
    p=re.compile(r'\w{3}\s\w{3}\s\s\d\s\d{2}\:\d{2}\:\d{2}\s\d{4}\s{3}(\d{2}\.\d{2}\.\d{2}\.\d{2})\s{3}([POST]+|[GET]+)\s\/')
    # print(p.match("Mon Feb  5 10:47:12 2018   46.38.92.44   POST /"))
    for i in range(len(list)):
        i=p.match(list[i])
        print(i.group(1))
    
def ration_get(list):
    post_num=0
    get_num=0
    p=re.compile(r'\w{3}\s\w{3}\s\s\d\s\d{2}\:\d{2}\:\d{2}\s\d{4}\s{3}\d{2}\.\d{2}\.\d{2}\.\d{2}\s{3}([POST]+|[GET]+)\s\/')
    for i in range(len(list)):
        i=p.match(list[i])
        print(i.group(1))
        if i.group(1) == 'POST':
            post_num +=1
        else:
            get_num += 1
            
    print(post_num,get_num)
    ration =get_num / post_num
    print(ration) 

list=logs()
array_get(list)
ration_get(list)