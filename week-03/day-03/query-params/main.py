from flask import Flask, render_template, request
import csv

app = Flask(__name__)


@app.route('/')
def get_data():
  params = request.args
  key = params.get('key')
  value = params.get('value')
  results = []
  if key and value:
    data = read_csv_file('./data/products.csv')
    for item in data:
      if key in ['price', 'qty']:
        if item[key] > value:
          results.append(item)
      else:
        if value in item[key]:
          results.append(item)

  return render_template('index.html', results=results, params=params)



def read_csv_file(file_name):
  try:
    with open(file_name, 'r') as file:
      line_list = []
      reader = csv.DictReader(file, delimiter=';')
      for row in reader:
        line_list.append(row)
      return line_list
  except Exception as e:
    print(f'Error occurs when reading file {file_name}: {e}')
    return False
