import psycopg2
import sys
from db_service import create_todo_table, list_all, insert_to_table, get_record_table, remove_record_table

action_dic = {
  'list': '-l',
  'add': '-a',
  'check': '-c',
  'remove': '-r'
}

def get_second_arg(arg):
  if len(arg) >= 3:
    return arg[2]
  else:
    raise TypeError(f'Your {arg[1]} must fellow a args')

connection = psycopg2.connect(user='lwj',
                              password='lwj',
                              host='127.0.0.1',
                              port='5432',
                              database='lwj')
cursor = connection.cursor()
# print(connection.get_dsn_parameters(),"\n")
# create_todo_table(connection)

if (len(sys.argv) > 1):
  action = sys.argv[1]
  if action == action_dic['list']:
    todos = list_all(cursor)
    for todo in todos:
      print(f'{str(todo[0])} status- {todo[1]}, des- {todo[2]}')
  elif action == action_dic['add']:
    try:
      arg_2 = get_second_arg(sys.argv)
      insert_to_table(cursor, connection, arg_2)
    except TypeError as error:
      print(error)
  elif action == action_dic['check']:
    try:
      arg_2 = get_second_arg(sys.argv)
      todo = get_record_table(cursor, arg_2)
      print(todo)
    except TypeError as error:
      print(error)
  elif action == action_dic['remove']:
    try:
      arg_2 = get_second_arg(sys.argv)
      remove_record_table(cursor, connection, arg_2)
    except TypeError as error:
      print(error)

cursor.close()
connection.close()


