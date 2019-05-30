from db.connection import connect_db
import json

def write_to_js_file(file_name, data):
  with open(file_name, 'w') as outfile:
    outfile.write('export default')
    json.dump(data, outfile)

def count_msg_by_user():
  connection = connect_db()
  cursor = connection.cursor()
  query = 'SELECT user_id, count(*) as msg_counter FROM messages GROUP BY user_id ORDER BY msg_counter DESC;'
  cursor.execute(query)
  result = cursor.fetchall()
  cursor.close()
  connection.close()
  data = []
  for item in result:
    data.append({
      'user_id': item[0],
      'count': item[1]
    })
  return data

def count_reactions():
  connection = connect_db()
  cursor = connection.cursor()
  query = 'SELECT reaction, count(*) as counter FROM reactions GROUP BY reaction ORDER BY counter desc;'
  cursor.execute(query)
  result = cursor.fetchall()
  cursor.close()
  connection.close()
  data = []
  for item in result:
    data.append({
      'reaction': item[0],
      'count': item[1]
    })
  return data

def reaction_user_counter():
  connection = connect_db()
  cursor = connection.cursor()
  query = 'SELECT user_id, count(*) as counter FROM reactions GROUP BY user_id ORDER BY counter desc;'
  cursor.execute(query)
  result = cursor.fetchall()
  cursor.close()
  connection.close()
  data = []
  for item in result:
    data.append({
      'user_id': item[0],
      'count': item[1]
    })
  return data


def avg_msg_counter_hour_day():
  connection = connect_db()
  cursor = connection.cursor()
  query = "select time_hour, count(*) as counter from (select date_part('hour', sent_at) as time_hour from messages) tmp group by time_hour order by time_hour;"
  cursor.execute(query)
  result = cursor.fetchall()
  query_2 = "select to_char(sent_at, 'mm-dd-yyyy') as date from messages order by sent_at limit 1;"
  query_3 = "select to_char(sent_at, 'mm-dd-yyyy') as date from messages order by sent_at  desc limit 1;"
  cursor.execute(query_2)
  start_date = cursor.fetchone()
  cursor.execute(query_3)
  end_date = cursor.fetchone()
  cursor.close()
  connection.close()
  data = []
  for item in result:
    data.append({
      'hour': int(item[0]),
      'count': item[1]
    })
  return [data, start_date[0], end_date[0]]