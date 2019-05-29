def create_todo_table(connection):
  cursor = connection.cursor()
  todo_table_exsiting = cursor.execute("select * from information_schema.tables where table_name=%s", ('todo',))
  if not bool(todo_table_exsiting):
    create_table_query = '''CREATE TABLE todo
                (id  SERIAL PRIMARY KEY,
                state TEXT    NOT NULL,
                description TEXT,
                CONSTRAINT chk_state CHECK (state IN ('TODO', 'IN_PROCESS', 'DONE'))
                ); '''
    cursor.execute(create_table_query)
    connection.commit()
    cursor.close()

# read

def list_all(cursor):
  select_query = 'SELECT * FROM todo'
  cursor.execute(select_query)
  return cursor.fetchall()

# insert

def insert_to_table(cursor, connection, arg_2):
  insert_query = 'INSERT INTO todo(state, description) VALUES(%s, %s)'
  todo = {
    'state': 'TODO',
    'description': arg_2
  }
  cursor.execute(insert_query, (todo['state'], todo['description']))
  connection.commit()

# check one

def get_record_table(cursor, arg_2):
  select_query = 'SELECT * from todo where id=%s'
  cursor.execute(select_query, (arg_2, ))
  return cursor.fetchone()

# delete


def remove_record_table(cursor, connection, arg_2):
  delete_query = 'DELETE from todo WHERE id=%s'
  cursor.execute(delete_query, (arg_2,))
  connection.commit()
