from db import connect, create_music_table, list_all, list_by_attr, remove_record_table, insert_to_table, update_record_table
import sys


def search_music(connection, args):
  if len(args) == 0:
    print(list_all(connection))
  elif len(args) == 1:
    print(list_by_attr(connection, {'title': args[0], 'artist': args[0]}))
  elif len(args) == 2:
    search_query = {}
    if args[0] == '--artist':
      search_query = { 'artist': args[1] }
    elif args[0] == '--title':
      search_query = { 'title': args[1] }
    print(list_by_attr(connection, search_query))
  else:
    print('Not valid command')

def add_a_music(connection, args):
  insert_dic = {}
  if len(args) == 2:
    if args[0].endswith(','):
      insert_dic['artist'] = args[0].split(',')[0]
      insert_dic['title'] = args[1]
    elif args[0].endswith(':'):
      insert_dic['artist'] = args[0].split(':')[0]
      insert_dic['title'] = args[1]
    else:
      print('invalid command')
    
  elif len(args) == 4:
    if args[0] == '--artist' and args[2] == '--title':
      insert_dic['artist'] = args[1]
      insert_dic['title'] = args[3]
    elif args[0] == '--title'and args[2] == '--artist':
      insert_dic['artist'] = args[3]
      insert_dic['title'] = args[1]
    else:
      print('invalid command')
  if not not insert_dic:
    insert_to_table(connection, insert_dic)

def remove_a_music(connection, args):
  if len(args) >= 1:
    print(int(args[0]))
    remove_record_table(connection, int(args[0]))
  else:
    print('Not valid command')


in_process_song_id = -1
def play_a_music(connection, args):
  global in_process_song_id
  if len(args) == 1:
    if in_process_song_id > 0:
      update_record_table(connection, {'id': in_process_song_id}, 'DONE')
    in_process_song_id = int(args[0])
    update_record_table(connection, {'id': in_process_song_id}, 'IN_PROCESS')

command = {
  'l': search_music,
  'a': add_a_music,
  'r': remove_a_music,
  'p': play_a_music
}
def main_process():
  connection = connect()
  create_music_table(connection)
  while(True):
    input_str = input('Please input a number(press enter to end):\n')
    input_str_list = input_str.split()
    if len(input_str_list) > 0:
      command[input_str_list.pop(0)](connection, input_str_list)
  connection.close()


main_process()
