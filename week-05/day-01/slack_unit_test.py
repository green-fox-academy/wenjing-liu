import unittest
from datetime import datetime

from slack import parseMsgs, parseMentions, parseReactions, parseUsers, parseData, Message, User,Mention, Reaction

class TestCounter(unittest.TestCase):
  def setUp(self):
    self.test_data = [{
      "client_msg_id": "2e3e16f0-928e-4ad9-b28a-3a29f1f2f01d",
      "type": "message",
      "text": "<@UDZNG4FL7> thank you the typo, it made my day :pray::joy:",
      "user": "UB1ATRBQV",
      "ts": "1558973913.006400",
      "thread_ts": "1558973913.006400",
      "reply_count": 1,
      "reply_users_count": 1,
      "latest_reply": "1558974232.007700",
      "reply_users": [ "UDZNG4FL7"],
      "replies": [
        {
        "user": "UDZNG4FL7",
        "ts": "1558974232.007700"
        }
      ],
      "subscribed": False,
      "reactions": [
        {
        "name": "smile",
        "users": [ "UDZNG4FL7", "UGLGS3TQS", "UC7JZG36C", "U15CJU8U8", "UEGB506PJ", "UB29NHSKH" ],
        "count": 6
        }
      ]
      }
    ]
  
  def test_parseMsgs(self):
    result = parseMsgs(self.test_data)
    msg = Message(id=self.test_data[0]['client_msg_id'], user_id=self.test_data[0]['user'], message=self.test_data[0]['text'],sent_at=datetime.fromtimestamp(float(self.test_data[0]['ts'].split('.')[0])))
    self.assertEqual(len(result), 1)
    self.assertEqual(msg, result[0])
  
  def test_parseMentions(self):
    result = parseMentions(self.test_data)
    mention = Mention(message_id=self.test_data[0]['client_msg_id'], user_id='UDZNG4FL7')
    self.assertEquals(len(result), 1)
    self.assertEqual(mention, result[0])
  
  def test_parseReactions(self):
    result = parseReactions(self.test_data)
    aim_result = []
    for reaction in self.test_data[0]['reactions']:
      for user in reaction['users']:
        aim_result.append(Reaction(message_id=self.test_data[0]['client_msg_id'], user_id=user, reaction=reaction['name']))
    self.assertEqual(len(result), len(aim_result))
    self.assertEqual(result, aim_result)
  
  def test_parseUsers(self):
    msg = [Message(id=self.test_data[0]['client_msg_id'], user_id=self.test_data[0]['user'], message=self.test_data[0]['text'],sent_at=datetime.fromtimestamp(float(self.test_data[0]['ts'].split('.')[0])))]
    mentions = [Mention(message_id=self.test_data[0]['client_msg_id'], user_id='UDZNG4FL7')]
    reactions = []
    for reaction in self.test_data[0]['reactions']:
      for user in reaction['users']:
        reactions.append(Reaction(message_id=self.test_data[0]['client_msg_id'], user_id=user, reaction=reaction['name']))
    msg.extend(mentions)
    msg.extend(reactions)
    users = parseUsers(msg)
    self.assertEqual(len(users), 7)

  def test_parseData(self):
    result = parseData(self.test_data)
    msg = Message(id=self.test_data[0]['client_msg_id'], user_id=self.test_data[0]['user'], message=self.test_data[0]['text'],sent_at=datetime.fromtimestamp(float(self.test_data[0]['ts'].split('.')[0])))
    mention = Mention(message_id=self.test_data[0]['client_msg_id'], user_id='UDZNG4FL7')
    reactions = []
    for reaction in self.test_data[0]['reactions']:
      for user in reaction['users']:
        reactions.append(Reaction(message_id=self.test_data[0]['client_msg_id'], user_id=user, reaction=reaction['name']))
    self.assertEqual(result[0], [msg])
    self.assertEqual(len(result[1]), 7)
    self.assertEqual(result[2], [mention])
    self.assertEqual(result[3], reactions)

  
if __name__ == '__main__':
    unittest.main()