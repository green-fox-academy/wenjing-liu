import csv
import json
import xml.etree.ElementTree as xml


def transform_csv_json(src, des):
  try:
    with open(src, 'r') as file:
      with open(des, 'w') as outfile: 
        line_list = []
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
          line_list.append(row)
        json.dump(line_list, outfile)
  except Exception as e:
    print(f'Error occurs when reading file {src}: {e}')
    return False


def transform_json_xml(src, des):
  with open(src, 'r') as file:
    data = json.load(file)
    root = xml.Element('Flowers')
    for index in range(len(data)):
      flower = xml.Element('flower')
      root.append(flower)
      for key, value in data[index].items():
        sub_element = xml.SubElement(flower, str(key))
        sub_element.text = str(value)
      tree = xml.ElementTree(root)
      tree.write(des)
      


transform_csv_json('users.csv', 'users_csv_json.json')
transform_json_xml('flowers.json', 'flowers_json_xml.xml')