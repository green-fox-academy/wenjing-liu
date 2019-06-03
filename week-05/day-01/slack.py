"""
# Slack

Try to parse the Slack Project's data with functional programming principles in
mind. Write unit tests as well. You don't need to store it in the database.
"""
import collections
import json
from datetime import datetime
import re
from functools import reduce

mention_pattern = re.compile(r'<@(\w{9})>')
def read_file(src_file):
  with open(src_file, 'r') as file:
    content = json.load(file)
    return content

Message = collections.namedtuple('Message', 'id user_id message sent_at')
User = collections.namedtuple('User', 'id')
Mention = collections.namedtuple('Mention', 'message_id user_id')
Reaction = collections.namedtuple('Reaction', 'message_id user_id reaction')

def mention(item):
  return map(lambda user: Mention(message_id=item['client_msg_id'], user_id=user), mention_pattern.findall(item['text']))

def reaction(item):
  result = []
  for reaction in item['reactions']:
    result.extend(list(map(lambda user: Reaction(message_id=item['client_msg_id'], user_id=user, reaction= reaction['name']), reaction['users'])))
  return result


def parseMsgs(data):
  return list(map(lambda item: Message(id=item['client_msg_id'], user_id=item['user'], message=item['text'], sent_at=datetime.fromtimestamp(float(item['ts'].split('.')[0]))), data))

def parseMentions(data):
  m_list = list(map(lambda item: list(mention(item)), data))
  return list(reduce(lambda x, y: y + x, m_list))

def parseReactions(data):
  data_r = filter(lambda item: 'reactions' in item, data)
  r_list = list(map(lambda item: reaction(item), data_r))
  return list(reduce(lambda x, y: x + y, r_list))

def parseUsers(data_list):
  user_set = set()
  user_set.update(map(lambda x: x.user_id, data_list))
  return list(map(lambda user: User(id=user), user_set))

def parseData(raw_data):
  data = list(filter(lambda item: 'client_msg_id' in item and 'user' in item, raw_data))
  msgs = parseMsgs(data)
  mentions = parseMentions(data)
  reactions = parseReactions(data)
  users = parseUsers(list(reduce(lambda x, y: x+y, [msgs, mentions, reactions])))
  return [msgs, users, mentions, reactions]


def load_data(file_path):
  raw_data = read_file(file_path)
  [msgs, users, mentions, reactions] = parseData(raw_data)
  print('msgs length: ', len(msgs))
  print('users length: ', len(users))
  print('mentions length: ', len(mentions))
  print('reactions length: ', len(reactions))



# load_data('./slack_data.json')