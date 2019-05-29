import json
import psycopg2


def read_file(src_file):
  with open(src_file, 'r') as file:
    content = json.load(file)
    return content


def connect_db():
  connection = psycopg2.connect(user='lwj',
                              password='lwj',
                              host='127.0.0.1',
                              port='5432',
                              database='lwj')
  return connection

def create_car_table(connection):
  cursor = connection.cursor()
  create_table_query = '''CREATE TABLE IF NOT EXISTS car
                (id  SERIAL PRIMARY KEY,
                brand varchar(50),
                model varchar(50),
                year int,
                condition varchar(200),
                price int,
                count int
                );'''
  cursor.execute(create_table_query)
  connection.commit()
  cursor.close()

  


def migrate_to_db(connection, data):
  cursor = connection.cursor()
  insert_query = 'INSERT INTO car VALUES(%s,%s,%s,%s,%s,%s,%s)'
  for car in data:
    cursor.execute(insert_query, (car['id'], car['brand'], car['model'], car['year'], car['condition'], car['price'], car['count']))
  connection.commit()
  cursor.close()

def remove_no_stock_car(connection):
  cursor = connection.cursor()
  delete_query = 'DELETE from car WHERE count = 0'
  cursor.execute(delete_query)
  connection.commit()
  cursor.close()


def discount_wreck_car(connection):
  cursor = connection.cursor()
  update_query = "UPDATE car SET price = 0.8 * price WHERE condition='wreck';"
  cursor.execute(update_query)
  connection.commit()
  cursor.close()

def avg_age_car(connection):
  cursor = connection.cursor()
  select_query = "SELECT avg(date_part('year', CURRENT_DATE) - year) from car;"
  cursor.execute(select_query)
  result = cursor.fetchone()
  cursor.close()
  return result[0]





def main_process():
  connection = connect_db()
  create_car_table(connection)
  data = read_file('./cars.json')
  migrate_to_db(connection, data)
  remove_no_stock_car(connection)
  discount_wreck_car(connection)
  print(avg_age_car(connection))
  connection.close()


main_process()
