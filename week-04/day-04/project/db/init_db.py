from connection import connect_db
from models import create_users_table, create_messages_table, create_mentions_table, create_reactions_table, create_channels_table



def init_db():
  connection = connect_db()
  if not connection:
    raise ReferenceError('Database is not connected')
  create_users_table(connection)
  create_channels_table(connection)
  create_messages_table(connection)
  create_mentions_table(connection)
  create_reactions_table(connection)
  connection.close()



def main_process():
  try:
    init_db()
  except ReferenceError as error:
    print(error)


main_process()

