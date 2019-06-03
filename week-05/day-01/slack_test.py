from slack import Slack
import unittest
from slack import get_data

class Test_Slack(unittest.TestCase):
    def test_users_num(self):
        jsondata = get_data()
        slack = Slack()
        param = slack.get_users_list(jsondata)
        self.assertEqual(len(slack.final_users(param)),83)

    def test_messages(self):
        jsondata = get_data()
        slack = Slack()
        param = slack.get_messages_list(jsondata)
        self.assertEqual(len(slack.final_message(param)),581)
    
    def test_mentions(self):
        jsondata =get_data()
        slack = Slack()
        param = slack.get_mentions_list(jsondata)
        self.assertEqual(len(slack.fian_mentions(param)),581)

if __name__ == "__main__":
    unittest.main()
