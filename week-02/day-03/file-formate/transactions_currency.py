# from xml.dom import minidom
import xml.etree.ElementTree as ET 

def find_transaction_currency(file_name, currency_name):
  tree = ET.parse(file_name)
  root = tree.getroot()
  filtered_trans = []
  for element in root:
    for child in element:
      if child.tag == 'amount' and child.attrib['currency'] == currency_name:
         filtered_trans.append(element)
  return filtered_trans


transactions = find_transaction_currency('transactions.xml', 'USD')
for tras in transactions:
  for child in tras:
    print(f'{child.tag}: {child.text} USD', end = ' ')
  print()

