import json
import csv
import xml.etree.ElementTree as ET 
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

def create_employee_table(connection):
  cursor = connection.cursor()
  create_table_query = '''CREATE TABLE IF NOT EXISTS employees
                (id SERIAL PRIMARY KEY,
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                birth_date DATE, 
                gender VARCHAR(50),
                monthly_salary NUMERIC);'''
  cursor.execute(create_table_query)
  connection.commit()
  cursor.close()



def read_csv_file(src_file):
  with open(src_file, 'r') as file:
    line_list = []
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
      line_list.append(row)
  return line_list

def read_json_file(src_file):
  with open(src_file, 'r') as file:
    content = json.load(file)
    for item in content:
      item['first_name'] = item['name'].split(' ')[0]
      item['last_name'] = item['name'].split(' ')[1]
  return content

def read_xml_file(src_file):
  tree = ET.parse(src_file)
  root = tree.getroot()
  children = list(root)
  data = []
  for child in children:
    row = {}
    for element in child:
      if element.tag == 'salary_by_year':
        row['monthly_salary'] = float(element.text)/12
      if element.tag == 'name':
        row['first_name'] = element.text.split(' ')[0]
        row['last_name'] = element.text.split(' ')[1]
      else:
        row[element.tag] = element.text
    data.append(row)
  return data

def migrate_to_db(connection, data):
  cursor = connection.cursor()
  insert_query = 'INSERT INTO employees(first_name, last_name, birth_date, gender, monthly_salary) VALUES(%s,%s,%s,%s,%s)'
  for employee in data:
    cursor.execute(insert_query, (employee['first_name'], employee['last_name'],employee['birth_date'], employee['gender'],employee['monthly_salary']))
  connection.commit()
  cursor.close()



def db_manipulation(connection):
  cursor = connection.cursor()
  # - Which first name is the most common in the company?
  tmp_query = 'SELECT first_name, COUNT(*) AS counter FROM employees GROUP BY first_name'
  max_select_query = f'''SELECT first_name FROM ({tmp_query}) AS tmp_1
  JOIN (SELECT MAX(counter) AS max_counter FROM ({tmp_query}) AS tmp)  tmp_2
  ON tmp_1.counter = tmp_2.max_counter;'''
  cursor.execute(max_select_query)
  most_common_names = cursor.fetchall()
  print('Which first name is the most common in the company? ', most_common_names)
 
  # - Which first name is the most common among the younger (<30) employees?
  tmp_query_2 = "SELECT first_name, COUNT(*) AS counter FROM employees WHERE date_part('year',CURRENT_DATE) - date_part('year', birth_date) <= 30 GROUP BY first_name order by counter"
  max_select_query_2 = f'''SELECT first_name FROM ({tmp_query_2}) AS tmp_1
  JOIN (SELECT MAX(counter) AS max_counter FROM ({tmp_query_2}) AS tmp)  tmp_2
  ON tmp_1.counter = tmp_2.max_counter;'''
  cursor.execute(max_select_query_2)
  most_common_names = cursor.fetchall()
  print('Which first name is the most common among the younger (<30) employees?\n', most_common_names)

  # - What is the median salary in the company?
  query_median = 'SELECT avg(monthly_salary) FROM employees;'
  cursor.execute(query_median)
  print('What is the median salary in the company? ', cursor.fetchone()[0])

  # - How many employee earns more than the average?
  #   - do not hard-code the average
  #   - use one query
  query_more_than_median = 'select count(*) from (select * from employees, (SELECT avg(monthly_salary)as avg FROM employees) as tmp where employees.monthly_salary > tmp.avg) tmp;'
  cursor.execute(query_more_than_median)
  print('How many employee earns more than the average? ',cursor.fetchone()[0])

  # - Increase the salary by monthly $100 for everybody who earns less than the median

  increase_salary_query = 'UPDATE employees SET monthly_salary = monthly_salary + 100 WHERE monthly_salary < (SELECT avg(monthly_salary)as avg FROM employees);'
  cursor.execute(increase_salary_query)
  connection.commit()
  print('Increase the salary by monthly $100 for everybody who earns less than the median: ', cursor.rowcount, ' employees update')

  cursor.close()



def main_process():
  connection = connect_db()
  create_employee_table(connection)
  data = []
  data.extend(read_csv_file('./employees.csv'))
  data.extend(read_json_file('./employees.json'))
  data.extend(read_xml_file('./employees.xml'))
  migrate_to_db(connection, data)
  db_manipulation(connection)
  connection.close()



main_process()
