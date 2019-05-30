
def create_users_table(connection):
  cursor = connection.cursor()
  create_query = '''CREATE TABLE IF NOT EXISTS users
              (id  VARCHAR(20) PRIMARY KEY,
              name VARCHAR(128)
              ); '''
  cursor.execute(create_query)
  connection.commit()
  cursor.close()


def create_messages_table(connection):
  cursor = connection.cursor()
  create_query = ''
  create_query = '''CREATE TABLE IF NOT EXISTS messages
              (id  VARCHAR(50) PRIMARY KEY,
              user_id VARCHAR(20) NOT NULL,
              message TEXT,
              channel_id int,
              sent_at TIMESTAMP
              ); '''
  cursor.execute(create_query)
  connection.commit()
  cursor.close()

def create_mentions_table(connection):
  cursor = connection.cursor()
  create_query = ''
  create_query = '''CREATE TABLE IF NOT EXISTS mentions
              (id  SERIAL PRIMARY KEY,
              user_id VARCHAR(20) NOT NULL,
              message_id VARCHAR(50) NOT NULL
              ); '''
  cursor.execute(create_query)
  connection.commit()
  cursor.close()

def create_reactions_table(connection):
  cursor = connection.cursor()
  create_query = '''CREATE TABLE IF NOT EXISTS reactions
              (id  SERIAL PRIMARY KEY,
              user_id VARCHAR(20) NOT NULL,
              message_id VARCHAR(50) NOT NULL,
              reaction VARCHAR(128)
              ); '''
  cursor.execute(create_query)
  connection.commit()
  cursor.close()


def create_channels_table(connection):
  cursor = connection.cursor()
  create_query = '''CREATE TABLE IF NOT EXISTS channels
              (id  SERIAL PRIMARY KEY,
              name TEXT NOT NULL
              ); '''
  cursor.execute(create_query)
  connection.commit()
  cursor.close()

  