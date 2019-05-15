import csv

f=open('election.csv','r')
csvreader = csv.reader(f)
final_list=list(csvreader)

for i in range(len(final_list)):
    if "" not in final_list[i] and len(final_list[i]) == 4:
        print(final_list[i])


