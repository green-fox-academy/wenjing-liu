from flask import Flask, render_template
import requests
import pandas as pd

API_URL = 'http://api.zoopla.co.uk/api/v1/'


url='https://api.zoopla.co.uk/api/v1/'
api_key='9dud55d9tr4ptf7umqt4rmf6'
params = {
  'page_size': 1,
  'page_number': 1,
  'listing_status': 'sale',
  'include_sold': 1,
  'area': 'Somerset'
}

action = 'property_listings.json'
params.update({'api_key': api_key})
response = requests.get(API_URL + action, params)
print(response)
if response.ok:
  json = response.json()
  print(json)
  df = pd.DataFrame(json['listing'])
  df.to_json('tmp.json', orient='split')
  
