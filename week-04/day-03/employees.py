import json
import csv
from xml.dom import minidom
import psycopg2

con=psycopg2.connect(
    host='localhost',
    database='Angela_Datebase',
    user='postgres',
    password='1234'
)
cursor = con.cursor()
# transform the employees.json into postgres
with open('employees.json') as f:
    data=f.read()
    jsondata=json.loads(data)

for json in jsondata:
    name = json["name"].split( )
    id = json["id"]
    first_name=name[0]
    last_name=name[1]
    gender=json["gender"]
    monthly_salary=json["monthly_salary"]
    birth_date = json["birth_date"]
    insert_query = 'INSERT INTO employees_table VALUES (%s,%s,%s,%s,%s,%s)'
    # cursor.execute(insert_query,(id,first_name,last_name,gender,monthly_salary,birth_date))
con.commit()

# transform the employees.csv into postgres
f=open('employees.csv','r')
csvreader = csv.reader(f)
final_list=list(csvreader)
f.close
final_list.remove(final_list[0])
for employee in final_list:
    id=int(employee[0])+100
    first_name=employee[1]
    last_name=employee[2]
    gender=employee[4]
    monthly_salary=employee[5]
    bitrh_date = employee[3]
    insert_query = 'INSERT INTO employees_table VALUES (%s,%s,%s,%s,%s,%s)'
    # cursor.execute(insert_query,(id,first_name,last_name,gender,monthly_salary,bitrh_date))
con.commit()

# transform the employees.xml into postgres
dom=minidom.parse("employees.xml")
ids=dom.getElementsByTagName("id")
names=dom.getElementsByTagName("name")
genders=dom.getElementsByTagName("gender")
salary_by_year=dom.getElementsByTagName("salary_by_year")
bitrh_dates=dom.getElementsByTagName("birth_date")

id_list=[]
for i in range(len(ids)):
    id_list.append(ids[i].firstChild.data)

first_name_list=[]
last_name_list=[]
for i in range(len(names)):
    name=(names[i].firstChild.data).split( )
    first_name=name[0]
    first_name_list.append(first_name)
    last_name=name[1]
    last_name_list.append(last_name)

gender_list=[]
for i in range(len(genders)):
    gender_list.append(genders[i].firstChild.data)

salary_by_month=[]
for i in range(len(salary_by_year)):
    month_salary=int((salary_by_year[i].firstChild.data))/12
    salary_by_month.append(int(month_salary))

bitrh_date_list=[]
for i in range(len(bitrh_dates)):
    bitrh_date_list.append(bitrh_dates[i].firstChild.data)


for i in range(len(ids)):
    id=int(id_list[i])+200
    first_name=first_name_list[i]
    last_name=last_name_list[i]
    gender=gender_list[i]
    monthly_salary = salary_by_month[i]
    bitrh_date = bitrh_date_list[i]
    insert_query ='INSERT INTO employees_table VALUES (%s,%s,%s,%s,%s,%s)'
    # cursor.execute(insert_query,(id,first_name,last_name,gender,monthly_salary,bitrh_date))

con.commit()

# Which first name is the most common in the company?
def first_name_popular():
    select_query='SELECT DISTINCT first_name,count(*) FROM employees_table GROUP BY first_name'
    cursor.execute(select_query)
    first_name_count = cursor.fetchall()
    most_popular_first_name=0
    for i in range(len(first_name_count)):
        if first_name_count[i][1] > most_popular_first_name:
            most_popular_first_name = first_name_count[i][1]
    print(f'the most popular first name is {first_name_count[i][0]}')

    


first_name_popular()






select_query ='SELECT * FROM employees_table'
cursor.execute(select_query)
# print(cursor.fetchall())

cursor.close()
con.close()