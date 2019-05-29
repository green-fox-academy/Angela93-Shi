import psycopg2,sys
import re

con=psycopg2.connect(
    host='localhost',
    database='Angela_Datebase',
    user='postgres',
    password='1234'
)
cursor = con.cursor()

# Add a song
p=re.compile(r'(.+)[:,]\s(.+)')
if sys.argv[1] =='a' and len(sys.argv) == 3:
    get_song=sys.argv[2]
    m=p.match('Ed Sheeran: I Don\'t care')
    artist=m.group(1)
    title=m.group(2)
    status='playing'
    insert_query = 'INSERT INTO music_player VALUES (%s,%s,%s)'
    # cursor.execute(insert_query,(artist,title,status))
    con.commit()

# print(s.match(" --artist 'Ed Sheeran' --title 'I Don\'t care' "))
elif sys.argv[1] =='a' and len(sys.argv) == 6:
    artist=sys.argv[3]
    title=sys.argv[5]
    status='playing'
    insert_query = 'INSERT INTO music_player VALUES (%s,%s,%s)'
    cursor.execute(insert_query,(artist,title,status))
    con.commit()


select_query ='SELECT * FROM music_player'
cursor.execute(select_query)
print(cursor.fetchall())

cursor.close()
con.close()