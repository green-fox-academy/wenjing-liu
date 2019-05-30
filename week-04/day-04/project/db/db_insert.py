from connection import connect_db
import json
import re
from datetime import datetime

mention_pattern = re.compile(r'<@(\w{9})>')

def read_file(src_file):
  with open(src_file, 'r') as file:
    content = json.load(file)
    return content


def format_message(item):
  message = {}
  users = []
  tmp_user_id_set = set()
  mentions = []
  reactions = []
  mentioned_users = mention_pattern.findall(item['text'])
  message = {
    'id': item['client_msg_id'],
    'user_id': item['user'],
    'message': item['text'],
    'sent_at': datetime.fromtimestamp(float(item['ts'].split('.')[0]))
  }
  tmp_user_id_set.add(item['user'])

  tmp_user_id_set.update(mentioned_users)

  
  for user in mentioned_users:
    mentions.append({
      'message_id': item['client_msg_id'],
      'user_id': user
    })
  
  if 'reactions' in item:
    for reaction in item['reactions']:
      for user in reaction['users']:
        tmp_user_id_set.add(user)
        reactions.append({
          'message_id': item['client_msg_id'],
          'user_id': user,
          'reaction': reaction['name']
        })
  
  for user in tmp_user_id_set:
    users.append({
      'id': user
    })
  return [message, users, mentions, reactions]


def insert_message(message, cursor):
  channel_id = cursor.execute("SELECT id FROM channels WHERE name= 'thanks channel'")
  insert_query = 'INSERT INTO messages(id, user_id, message, channel_id, sent_at) VALUES(%s, %s,%s,%s,%s) ON CONFLICT (id) DO NOTHING;'
  cursor.execute(insert_query, (message['id'], message['user_id'], message['message'], channel_id, message['sent_at']))

def insert_users(users, cursor):
  insert_query = 'INSERT INTO users(id) VALUES(%s) ON CONFLICT (id) DO NOTHING;'
  for user in users:
    cursor.execute(insert_query, (user['id'],))

def insert_mentions(mentions, cursor):
  insert_query = 'INSERT INTO mentions(message_id, user_id) VALUES(%s, %s)'
  for mention in mentions:
    cursor.execute(insert_query, (mention['message_id'], mention['user_id']))

def insert_reactions(reactions, cursor):
  insert_query = 'INSERT INTO reactions(message_id, user_id, reaction) VALUES(%s, %s, %s)'
  for reaction in reactions:
    cursor.execute(insert_query, (reaction['message_id'], reaction['user_id'], reaction['reaction']))

def insert_to_db():
  connection = connect_db()
  cursor = connection.cursor()
  data = read_file('./thanks_channel_history.json')
  for item in data:
    if 'client_msg_id' not in item or 'user' not in item:
      continue
    [message, users, mentions, reactions] = format_message(item)
    insert_message(message, cursor)
    insert_users(users, cursor)
    insert_mentions(mentions, cursor)
    insert_reactions(reactions, cursor)
    connection.commit()
  
  cursor.close()
  connection.close()

insert_to_db()