import json
import re

def get_data():
    with open('gfa_team_thanks.json') as f:
        data=f.read()
        jsondata = json.loads(data)
    return jsondata

class Slack:
    # extract the info for users
    def get_users_list(self,jsondata):
        self.jsondata = jsondata
        useful_list = list(filter(lambda item:'user' in item,jsondata))
        return useful_list
    
    def final_users(self,useful_list):
        self.useful_list = useful_list
        unique_list = set(map(lambda x: x['user'], useful_list))
        return unique_list
        
    # extract the info for messages
    def  get_messages_list(self,jsondata):
        self.jsondata = jsondata
        useful_messages = list(filter(lambda item: 'user' in item and 'client_msg_id' in item ,jsondata ))
        return useful_messages
    def final_message(self,useful_messages):
        self.useful_messages = useful_messages
        final_message = list(map(lambda x: [x['client_msg_id'],x['user'],x['ts']],useful_messages))
        return final_message

    # extract the info for mentions
    def get_mentions_list(self,jsondata):
        self.jsondata = jsondata
        useful_mentions = list(filter(lambda item:'text' in item and 'user' in item and 'client_msg_id' in item, jsondata))
        return useful_mentions
    def fian_mentions(self,useful_mentions1):
        p=re.compile(r"<@(\w{9})>")
        self.useful_mentions = useful_mentions
        final_mentions = list(map(lambda x: [ x['client_msg_id'],p.findall(x['text']) ],useful_mentions))
        return final_mentions


slack = Slack()
useful_list = slack.get_users_list(get_data())
slack.final_users(useful_list)

useful_messages = slack.get_messages_list(get_data())
slack.final_message(useful_messages)

useful_mentions = slack.get_mentions_list(get_data())
slack.fian_mentions(useful_mentions)
