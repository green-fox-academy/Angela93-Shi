import json
import psycopg2
import time,datetime
import re

con=psycopg2.connect(
    host='localhost',
    database='slack_channel_database',
    user='postgres',
    password='1234'
)
cursor = con.cursor()

with open('gfa_team_thanks.json') as f:
    data=f.read()
    jsondata = json.loads(data)
    jsondata.pop(599)

# inert data for table users
def users_opera():
    user_id_set = set()
    for json in jsondata:
        try:
            user_name = json['user']
            user_id_set.add(user_name)
        except:
            pass

    for index,user in enumerate(user_id_set):
        user_id = user
        insert_query = 'INSERT INTO users VALUES (%s,%s)'
        #cursor.execute(insert_query,(index+1,user_id))
    con.commit()

users_opera()

# inert data for table messages
def messages_opera():
    p=re.compile(r'(\d+)\.(\d+)')
    for json in jsondata:
        if 'client_msg_id' in json:
            message_id = json['client_msg_id']

            user_id = json['user']
            message = json['text']
            channel = 'thanks_channel'

            time_original=json['ts']
            time_part = (p.match(time_original)).group(1)
            time_local = time.localtime(int(time_part))
            dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
    
            insert_query = 'INSERT INTO messages VALUES (%s,%s,%s,%s,%s)'
            #cursor.execute(insert_query,(message_id,user_id,message,channel,dt))
            con.commit()

messages_opera()  


# inert data for table reacrions

def reaction_opera():
    insert_query = 'INSERT INTO reactions(user_id,message_id,reaction) VALUES (%s,%s,%s)'
    for json in jsondata:
        try:
            message_id = json['client_msg_id']
        except:
            pass
        if 'reactions' in json:
            reaction_block=json['reactions']
            for reaction in reaction_block: 
                users = reaction['users']
                for user in users:
                    cursor.execute(insert_query,(user,message_id,reaction['name']))
    con.commit()

# reaction_opera()

# inert data for table mentions
# s=re.compile(r'\<\@\w[9]\>')
def mentions_opera():
    for json in jsondata:
        if 'client_msg_id' in json:
            message_id = json['client_msg_id']
            # user_id=json['user']
            try:
                text=json['text']
                mentiond_user = re.findall(r"<@(\w{9})>",text)
            except:
                pass
            for user in mentiond_user:
                insert_query = 'INSERT INTO mentions VALUES (%s,%s)'
                # cursor.execute(insert_query,(message_id,user))
    con.commit()

mentions_opera()


# select_query ='SELECT * FROM users'
# cursor.execute(select_query)
# print(cursor.fetchall())


# Create views for the questions below

#question one :Who sent the most messages to the thanks channel?
get_view1='''
    CREATE VIEW vn AS
    SELECT user_id,count(user_id) AS num
    FROM messages
    GROUP BY user_id
    ORDER BY num DESC LIMIT 1
    '''
# cursor.execute(get_view1)

def most_messages():
    select_query1 = 'SELECT * FROM vn'
    cursor.execute(select_query1)
    result1=cursor.fetchall()
    # print(f'{result1[0][0]} sent the most messages to the channel, {result1[0][1]} times')
    return result1

most_messages()

#question two:Which emoji is the most common as reaction in the thanks channel?
get_view2='''
        CREATE VIEW emoji_most_popular AS
        SELECT reaction,count(reaction) AS num
        FROM reactions
        GROUP BY reaction
        ORDER BY num DESC LIMIT 1
        '''
cursor.execute(get_view2)
def most_emoji():
    select_query2 = 'SELECT * FROM emoji_most_popular'
    cursor.execute(select_query2)
    result2=cursor.fetchall()
    print(f'emoji {result2[0][0]} is the most common reaction, {result2[0][1]} times')
    return result2
most_emoji()

#question three:Who reacted to the most messages?
get_view3='''
        CREATE VIEW most_react AS
        SELECT user_id,count(user_id) AS num
        FROM reactions
        GROUP BY user_id
        ORDER BY num DESC LIMIT 1
        '''
# cursor.execute(get_view3)
def reacted_most():
    select_query3 = 'SELECT * FROM most_react'
    cursor.execute(select_query3)
    result3=cursor.fetchall()
    # print(f'{result3[0][0]} reacts most, {result3[0][1]} times')
    return result3

reacted_most()

#question four:Which day was the most active in the channel?
# 2019-05-28 00:18:33
s=re.compile(r'(\d{4}-\d{2}\d{2})\s\d{2}:\d{2}:\d{2}')
get_view3='''
        CREATE VIEW most_active AS
        SELECT to_date(to_char(sent_at, 'YYYY/MM/DD'), 'YYYY/MM/DD') AS date,count(*) AS num
        FROM messages
        GROUP BY Date
        ORDER BY num DESC LIMIT 1
        '''
# cursor.execute(get_view3)
def most_active():
    select_query4 = "SELECT * FROM most_active"
    cursor.execute(select_query4)
    result4=cursor.fetchall()
    #print(f'{result4[0][0]} is the most active, post messages {result4[0][1]} times')
    return result4
most_active()


# cursor.close()
# con.close()
