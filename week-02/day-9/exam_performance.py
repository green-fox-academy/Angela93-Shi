import csv
import re
csv.register_dialect('mydialect',delimiter='\t',quoting=csv.QUOTE_ALL)

exam_list=[]
with open('exams.tsv',) as csvfile:
    file_list = csv.reader(csvfile,'mydialect')
    for line in file_list:
        exam_list.append(line)
    # print(exam_list)

time_list=[]
for i in range(1,len(exam_list)):
    time_list.append(exam_list[i][2])
    if 'null' in time_list:
        time_list.remove('null')
print(time_list)
# str_convert='\n'.join(time_list)
p=re.compile(r'(?P<hour>\.?\d+[h,\:]?)(?P<miniute>\d{0,4}[m,\:]?)(?P<second>\d{0,4}s?)')
# print(p.match('3600s'))
for i in range(len(time_list)):
    i=p.match(time_list[i])
    print(i.group("hour"))









