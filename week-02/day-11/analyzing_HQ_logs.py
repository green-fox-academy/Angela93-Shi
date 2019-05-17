import csv
import re

f=open('logs.csv','r',encoding='utf-8')
csvreader = csv.reader(f)
final_list=list(csvreader)
f.close

p=re.compile(r'^\d+\,\d{4}\.\d{2}.\d{2}\.\s(\d{1,2}\:\d{1,2}\:\d{1,2})\,')
#print(p.match('1,2019.01.02. 9:21:49,Access granted,203,12,A66 - 04 FÕBEJÁRAT (F-1) Door #1,5,Czender András,0,,0,,00215:09895'))
list_time=[]
list_person=[]
list_person_arrived={}
for i in range(len(final_list)):
    list_date_time = final_list[i][1]
    log_name= final_list[i][7]
    if log_name not in list_person:
        list_person.append(log_name)
    list_person_arrived.update({final_list[i][1]:final_list[i][7]})

t=re.compile(r'\d{4}\.\d{2}.\d{2}\.\s(\d{1,2}\:\d{1,2}\:\d{1,2})')
sum_hour=0
sum_min=0
sum_sec=0
# print(len(list_person_arrived))
for i in range(len(list_person_arrived)):
    list_person_arrived_time = list_person_arrived.keys()
    list_person_arrived_time_str = ''.join(list_person_arrived_time)
    # figure the average time in for loop begin
    m=t.match(list_person_arrived_time_str)
    specific_time = m.group(1)
    hour_min_sec=specific_time.split(':')
    sum_hour += int(hour_min_sec[0])
    sum_min += int(hour_min_sec[1])
    sum_sec += int(hour_min_sec[2])
    # figure the average time in for loop end

    list_person_arrived_time_list = list(specific_time )
    print(list_person_arrived_time_list)


average_hour = int(sum_hour / len(list_person_arrived))
average_min = int(sum_min / len(list_person_arrived))
average_sec = int(sum_sec / len(list_person_arrived))
print(f"the average time is {average_hour}:{average_min}:{average_sec}")




