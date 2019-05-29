import json
import psycopg2
import datetime

con=psycopg2.connect(
    host='localhost',
    database='Angela_Datebase',
    user='postgres',
    password='1234'
)
cursor = con.cursor()
with open('cars.json') as f:
    data=f.read()
    jsondata=json.loads(data)
    
for json in jsondata:
    id = json["id"]
    brand=json["brand"]
    model=json["model"]
    year=json["year"]
    condition=json["condition"]
    price=json["price"]
    count=json["count"]
    insert_query = 'INSERT INTO cars VALUES (%s,%s,%s,%s,%s,%s,%s)'
    # cursor.execute(insert_query,(id,brand,model,year,condition,price,count))
con.commit()

# Remove the cars which are not on stock
def remove_cars():
    delete_query = 'DELETE FROM cars WHERE count = 0'
    cursor.execute(delete_query)
    con.commit()
    
remove_cars()

# Decrease the price of wrecks by 20%
def decrease_price():
    update_query = "UPDATE cars SET price = price*0.8 WHERE condition='wreck' "
    cursor.execute(update_query)
    con.commit()

decrease_price()

# Count the average age of the cars on the stock
current_year = datetime.datetime.now().year

def average_age():
    select_query = "SELECT AVG(year) FROM cars"
    cursor.execute(select_query)
    result=cursor.fetchall()
    for num in result:
        average_year= int(num[0])
        average_age = current_year - average_year
    print(f'the average age is {average_age}')
    con.commit()

average_age()

select_query ='SELECT * FROM cars'
cursor.execute(select_query)
# print(cursor.fetchall())

cursor.close()
con.close()