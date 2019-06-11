
from bs4 import BeautifulSoup
import requests
import pandas as pd 
import json
import datetime
from pandas.io.json import json_normalize

def get_data(url, params=None):
  page = requests.get(url, params=params)
  return BeautifulSoup(page.content, 'html.parser')



gaming_url = 'https://www.amazon.co.uk/b/?node=429886031&ref_=Oct_CateC_340831031_0&pf_rd_p=7f82985b-d737-52c9-9ccb-b4e571543b12&pf_rd_s=merchandised-search-4&pf_rd_t=101&pf_rd_i=340831031&pf_rd_m=A3P5ROKL5A1OLE&pf_rd_r=N900ATMWJTGJVZCZDZDX&pf_rd_r=N900ATMWJTGJVZCZDZDX&pf_rd_p=7f82985b-d737-52c9-9ccb-b4e571543b12'


def get_top_three_laptops(url):
  page = get_data(url)
  best_items = page.select('div.octopus-best-seller-card > div.octopus-pc-card-content .octopus-pc-item .octopus-pc-item-link .octopus-pc-asin-info-section')
  result = []
  for item in best_items:
    price_div = item.select('div.octopus-pc-asin-price-section .octopus-pc-asin-price')[0]
    price = price_div.select('.a-price-symbol')[0].text + price_div.select('.a-price-whole')[0].text + price_div.select('.a-price-fraction')[0].text
    
    pre_price = price
    pre_divs = item.select('div.octopus-pc-asin-price-section div:nth-child(2) .octopus-pc-asin-strike-price')
    if len(pre_divs) > 0:
      pre_div = pre_divs[0]
      pre_price = pre_div.select('span.a-text-strike')[0].text.replace(' ', '')
    
    name = item.select('.octopus-pc-asin-title span:first-child')[0].text.replace(' ', '')
    result.append({
      'lap_name': name,
      'lap_cur_price': price,
      'lap_pre_price': pre_price,
      'lap_type': 'Best Seller'
    })
  return result


def print_result(results):
  for result in results:
    print(f"{result['lap_name']}:\n {result['lap_cur_price']}(current price), {result['lap_pre_price']}(previous price)\n")
    

result = get_top_three_laptops(gaming_url)

# print_result(result)

df = pd.DataFrame(result)
df.to_json('laptop_from_amazon.json', orient='split')