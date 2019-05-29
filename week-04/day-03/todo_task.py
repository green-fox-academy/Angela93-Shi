import psycopg2,sys

con=psycopg2.connect(
    host='localhost',
    database='Angela_Datebase',
    user='postgres',
    password='1234'
)
cursor = con.cursor()
select_query = 'SELECT id,description FROM todo_task'

# List tasks
if sys.argv[1]== '-1':
    cursor.execute(select_query)
    todo_list=cursor.fetchall()
    for todo in todo_list:
        print(f'{todo[0]} - {todo[1]}')
    con.commit()

# Add task
elif sys.argv[1]== "a 'Feed the monkey'":
    id=4
    state='pending'
    description='Feed the monkey'

    insert_query = 'INSERT INTO todo_task VALUES (%s,%s,%s)'
    cursor.execute(insert_query,(id,state,description))
    con.commit()

# select_query = 'SELECT id,description FROM todo_task WHERE id=2'

# Check task
elif sys.argv[1]=='c':
    num =int(sys.argv[2])
    cursor.execute(select_query)
    todo_list=cursor.fetchall()
    for todo in todo_list:
        if num in todo:
            print(f'{todo_list[num-1][0]}- {todo_list[num-1][1]}')
    con.commit()

# Remove task
elif sys.argv[1]=='r':
    num =int(sys.argv[2])
    cursor.execute(select_query)
    todo_list=cursor.fetchall()
    for todo in todo_list:
        if num in todo:
            todo_list.remove(todo_list[num-1])
    print(todo_list)
    con.commit()


cursor.close()
con.close()