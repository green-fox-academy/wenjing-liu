import psycopg2

def connect_db():
  connection = psycopg2.connect(user='postgres',
                              password='postgres',
                              host='127.0.0.1',
                              port='5432',
                              database='slack')
  return connection