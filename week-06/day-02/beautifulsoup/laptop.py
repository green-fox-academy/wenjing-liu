
#%%
from bs4 import BeautifulSoup
import requests
import pandas as pd 
import json
import datetime
from pandas.io.json import json_normalize

baseUrl = 'https://www.alza.co.uk'
def get_data(url, params=None):
  page = requests.get(url, params=params)
  return BeautifulSoup(page.content, 'html.parser')


def get_three_category_urls():
  
  # Get laptop urls
  home_page = get_data(baseUrl)
  left_div = home_page.find_all('div', id='left')[0]
  a_tag = left_div.find_all('a', title='Laptops')[0]
  next_sib_div = a_tag.find_next_sibling()
  home_office_url = next_sib_div.find_all('a', text='Home & Office')[0]['href']
  gaming_url = next_sib_div.find_all('a', text='Gaming')[0]['href']
  professional_url = next_sib_div.find_all('a', text='Professional')[0]['href']

  return {'home_office_url': home_office_url, 'gaming_url': gaming_url, 'professional_url': professional_url}


def get_top_three_laptops(part_url):
  url = baseUrl + part_url
  page = get_data(url)
  main_div = page.find_all('div', id='boxc')[0]
  result = []
  boxes = main_div.select("div[id='boxes'] > div")
  for i in range(3):
    box = boxes[i]
    name = box.select('div.top a.name.browsinglink')[0].text
    price = box.select('div.price > .priceInner > .c2')[0].text
    previous_price = price
    pr_span = box.select('div.price > .priceInner > .npc > .np2')
    if pr_span:
      previous_price = pr_span[0].text
    result.append({
      'lap_name': name,
      'lap_cur_price': price,
      'lap_pre_price': previous_price
    })
  return result

def print_result(results):
  for result in results:
    print(f"{result['lap_name']}: {result['lap_cur_price']}(current price), {result['lap_pre_price']}(previous price)")


url = get_three_category_urls()
home_top_three = get_top_three_laptops(url['home_office_url'])
gaming_top_three = get_top_three_laptops(url['gaming_url'])
professional_top_three = get_top_three_laptops(url['professional_url'])

# print('Home & office:\n')
# print_result(home_top_three)

# print('\nGaming:\n')
# print_result(gaming_top_three)

# print('\nProfessional:\n')
# print_result(professional_top_three)

def add_type(type_name, item_list):
  for item in item_list:
    item['lap_type'] = type_name

add_type('Home & Office', home_top_three)
add_type('Gaming', gaming_top_three)
add_type('Professional', professional_top_three)

result = []
result.extend(home_top_three)
result.extend(gaming_top_three)
result.extend(professional_top_three)

df = pd.DataFrame(result)
df.to_json('laptop_alza.json', orient='split')
