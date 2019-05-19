import csv
import re

f=open('logs.csv','r',encoding='utf-8')
csvreader = csv.reader(f)
final_list=list(csvreader)
f.close


list_time=[]
list_person=[]
clock_time_list=[]
clock_time_dic={}
clock_record_dic={}
# t=re.compile(r'\d{4}\.\d{2}.(\d{2})\.\s(\d{1,2}\:\d{1,2}\:\d{1,2})')

user_id=set()
for i in range(len(final_list)):
    user_id.add(final_list[i][12])
# print(user_id)

log_time_person={}
for i in user_id:
    clock_time_list=[]
    for j in final_list:
        if j[12] == i:
            clock_time_list.append(j[1])
    log_time_person[i] = clock_time_list
# print(log_time_person)
# p1 = re.compile(r"^(2019.01.[\d]{2})")
# p2 = re.compile(r"([\d]{1,2}:[\d]{2}:[\d]{2})")
# p3 = re.compile(r"([\d]{1,2}):[\d]{2}:[\d]{2}")
p4 = re.compile(r"2019.01.([\d]{2})")
t=re.compile(r'\d{4}\.\d{2}.(\d{2})\.\s(\d{1,2}\:\d{1,2}\:\d{1,2})')

person_first_log_list=[]
sum_hour = 0
sum_min = 0
sum_sec = 0
for key in log_time_person:
    log_time_person_first_log={}
    log_date=set()
    for j in log_time_person[key]:
        if int(p4.match(j).group(1)) >= 14:
            log_date.add(p4.match(j).group(1))

    log_time_dic={}
    
    for i in log_date:
        log_times_list=[]
        for j in log_time_person[key]:
            if p4.match(j).group(1) == i:
                log_times_list.append(j)
        log_time_dic[i] = log_times_list

    first_clock_in_dic={}
    for day in log_time_dic:
        first_clock_in = log_time_dic[day][0]
        first_clock_in_dic[day] = first_clock_in
        log_time_person_first_log[key] = first_clock_in_dic
    person_first_log_list.append(log_time_person_first_log)
print(person_first_log_list)

for i in person_first_log_list:
    for j in i:
        date=i[j]
        for m in date:
            specific_date_time = date[m]
            specific_time= (t.match(specific_date_time)).group(2)
            hour_min_sec=specific_time.split(':')
        sum_hour += int(hour_min_sec[0])
        sum_min += int(hour_min_sec[1])
        sum_sec += int(hour_min_sec[2])

average_hour = int(sum_hour / len(person_first_log_list))
average_min = int(sum_min / len(person_first_log_list))
average_sec = int(sum_sec / len(person_first_log_list))
# print(average_min)    
# print(average_sec)
print(f"the average time is {average_hour}:{average_min}:{average_sec}")




        






