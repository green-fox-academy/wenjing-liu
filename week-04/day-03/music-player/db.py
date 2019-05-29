import psycopg2

def connect():
  connection = psycopg2.connect(user='lwj',
                              password='lwj',
                              host='127.0.0.1',
                              port='5432',
                              database='lwj')
  return connection


def create_music_table(connection):
  cursor = connection.cursor()
  create_table_query = '''CREATE TABLE IF NOT EXISTS music
              (id  SERIAL PRIMARY KEY,
              title VARCHAR(50) NOT NULL,
              status VARCHAR(50) NOT NULL DEFAULT('NOT_START'),
              artist VARCHAR(50),
              CONSTRAINT chk_state CHECK (status IN ('NOT_START', 'IN_PROCESS', 'DONE'))
              ); '''
  cursor.execute(create_table_query)
  connection.commit()
  cursor.close()

# list all or some

def list_all(connection):
  cursor = connection.cursor()
  select_query = 'SELECT * FROM music'
  cursor.execute(select_query)
  result = cursor.fetchall()
  cursor.close()
  return result

def list_by_attr(connection, search_dic):
  cursor = connection.cursor()
  select_query = 'SELECT * FROM music WHERE '
  str_list = []
  for key, value in search_dic.items():
    str_list.append(f"{key} LIKE '%{value}%'")
  for index in range(len(str_list)):
    if index != 0:
      select_query += ' OR '
    select_query += str_list[index]
  cursor.execute(select_query)
  result = cursor.fetchall()
  cursor.close()
  return result


# add a song

def insert_to_table(connection, insert_dic):
  cursor = connection.cursor()
  insert_query = 'INSERT INTO music(title, artist) VALUES(%s, %s)'
  cursor.execute(insert_query, (insert_dic['title'], insert_dic['artist']))
  connection.commit()


# delete a song
def remove_record_table(connection, id):
  cursor = connection.cursor()
  delete_query = 'DELETE from music WHERE id=%s'
  cursor.execute(delete_query, (id,))
  connection.commit()
  cursor.close()


# play a song

def update_record_table(connection, play_dic, status):
  cursor = connection.cursor()
  update_query = f"UPDATE music SET status='{status}' WHERE "
  if 'id' in play_dic:
    update_query += f"id={play_dic['id']}"
  else:
    pass
  cursor.execute(update_query)
  connection.commit()
  cursor.close()

