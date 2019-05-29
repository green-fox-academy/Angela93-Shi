import json
import csv
from xml.dom import minidom
import psycopg2
import datetime

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
    cursor.execute(insert_query,(id,first_name,last_name,gender,monthly_salary,birth_date))
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
    cursor.execute(insert_query,(id,first_name,last_name,gender,monthly_salary,bitrh_date))
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
    cursor.execute(insert_query,(id,first_name,last_name,gender,monthly_salary,bitrh_date))

con.commit()

# Which first name is the most common in the company?
def first_name_popular():
    select_query='SELECT first_name,count(*) AS num FROM employees_table GROUP BY first_name ORDER BY num DESC LIMIT 1'
    cursor.execute(select_query)
    first_name_count = cursor.fetchall()
    print(f'the most popular first name is {first_name_count[0][0]},appears {first_name_count[0][1]}')

first_name_popular()

# Which first name is the most common among the younger (<30) employees?
def younger_first_name_popular():
    select_query='SELECT first_name,count(*) AS num FROM employees_table WHERE (current_date - employees_table.birth_date)/365 < 30 GROUP BY first_name ORDER BY num DESC LIMIT 1'
    cursor.execute(select_query)
    first_name_count = cursor.fetchall()
    print(f'the most popular first name is {first_name_count[0][0]},appears {first_name_count[0][1]}')

younger_first_name_popular()

# How many employee earns more than the average? 
def employees_more_than_average():
    select_query =''' SELECT count(id) FROM employees_table 
                        WHERE monthly_salary > (
                            SELECT AVG (monthly_salary) FROM employees_table
                        )
                    '''
    cursor.execute(select_query)
    people_count = cursor.fetchall()
    print(f'there are {people_count[0][0]} people earns more that the average')

employees_more_than_average()

# Increase the salary by monthly $100 for everybody who earns less than the median
def increase_money():
    update_query=''' UPDATE employees_table SET monthly_salary = monthly_salary+100
                    WHERE monthly_salary < (
                        SELECT tab.monthly_salary FROM (
                            SELECT a1.id,a1.monthly_salary,COUNT(a2.monthly_salary) salary_Rank
                            FROM employees_table a1,employees_table a2
                            WHERE a1.monthly_salary < a2.monthly_salary
                            OR (a1.monthly_salary = a2.monthly_salary and a1.id =a2.id)
                            GROUP BY a1.id,a1.monthly_salary
                            ORDER BY a1.monthly_salary DESC
                        ) as tab 
                        WHERE tab.salary_Rank=(select count(*)/2 from employees_table)
                    )
                '''
    cursor.execute(update_query)

increase_money()


select_query ='SELECT * FROM employees_table'
cursor.execute(select_query)
# print(cursor.fetchall())

cursor.close()
con.close()