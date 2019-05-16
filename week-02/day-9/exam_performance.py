import csv
import re
csv.register_dialect('mydialect',delimiter='\t',quoting=csv.QUOTE_ALL)

exam_list=[]
with open('exams.tsv',) as csvfile:
    file_list = csv.reader(csvfile,'mydialect')
    for line in file_list:
        exam_list.append(line)
    # print(exam_list)
h=re.compile(r'(^\.?\d?)[h,\:]')
m=re.compile(r'([\d]+)m|\:([\d]+)\:')
s=re.compile(r'\:?(\d+)$|(\d+)s$')


ratio_list=[]
sum_list=[]
for i in range(1,len(exam_list)):
    sum=0.0
    if h.search(exam_list[i][2]):
        a=h.search(exam_list[i][2])
        hour=a.group(1)
        miniute_res=float(float(hour)*60)
        sum += miniute_res
        # print(sum)
    if m.search(exam_list[i][2]):
        a=m.search(exam_list[i][2])
        if a.group(1) != None:
            miniute_temp=a.group(1)
        else:
            miniute_temp=a.group(2)
        miniute_res=float(miniute_temp)
        sum += miniute_res
        # print(sum)
    if s.search(exam_list[i][2]):
        a=s.search(exam_list[i][2])
        if a.group(1) != None:
            seconds_temp=a.group(1)
        else:
            seconds_temp=a.group(2)
        miniute_res=float(float(seconds_temp)/60.0)
        sum += miniute_res
    if sum != 0:
        ratio=int(exam_list[i][1])/sum
    ratio_list.append(ratio)

# print(ratio_list)
highest_ratio=0.0
for i in range(len(exam_list)-1):
    # print(ratio_list[i])
    ratio_list_num = float(ratio_list[i])
    if ratio_list_num > highest_ratio:
        highest_ratio = ratio_list_num
print(i)
print(f"the {i+1} has the highest ratio {highest_ratio}")

    














