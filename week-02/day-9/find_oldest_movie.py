import csv
import re

f=open('movies.csv','r')
csvreader = csv.reader(f)
final_list=list(csvreader)
print(final_list)

for i in range(len(final_list)):
    movie_item=''.join(final_list[i])
    print(movie_item)

p=re.compile(r'.+\;(\d{4})\;.+')

movie_year=[]
for i in range(len(final_list)):
    str_convert = ''.join(final_list[i])
    i=p.match(str_convert)
    year=i.group(1)
    movie_year.append(year)
print(movie_year)
oldest_year=min(movie_year)
print(oldest_year)
print(final_list)

for i in range(len(final_list)):
    if oldest_year in final_list[i][0]:
        print(final_list[i])



    