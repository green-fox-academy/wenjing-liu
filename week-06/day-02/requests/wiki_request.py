# From: Bristol, UK
# To: Prague, CZ
# Time: within 5 days prior to 24.12
# No changes in flight
# cheapest
#%%
import requests
import pandas as pd 
import json
import datetime
from pandas.io.json import json_normalize

baseUrl = 'https://api.skypicker.com/'
def get_data(url, params, headers):
  raw_data = requests.get(url, params=params, headers = headers)
  return json.loads(raw_data.text)

def get_city(city, country):
  url = baseUrl + 'locations?'
  headers = { 'Content-Type': 'application/json' }
  params = {'term': city, 'locale': country, 'location_types': 'airport','limit': 10, 'active_only': True, 'sort': 'name' }
  json_data = get_data(url, params, headers)
  df = json_normalize(json_data)
  result = {'id': df.iloc[0]['locations'][0]['id'],
  'locale_code': df.iloc[0]['meta.locale.code'] }
  return result

def get_flights(from_fly, to_fly, date_from, date_to):
    url = baseUrl + 'aggregation_flights?'
    headers = {'X-API-Version': '2'}
    params = {
      'fly_from':from_fly['id'],
      'fly_to': to_fly['id'],
      'v': 3,
      'date_from': date_from,
      'date_to': date_to,
      # 'max_fly_duration': 6,
      'flight_type': 'oneway',
      'one_for_city': 0,
      'one_per_date': 1,
      'adults': 1,
      'children':0,
      'infants': 0,
      'fly_days': [0,1,2,3,4,5,6],
      'fly_days_type': 'departure',
      # 'only_working_days': 0,
      # 'only_weekends': 0,
      # 'partner':'picky',
      # 'partner_market':'us',
      'curr':'EUR',
      'locale': 'en',
      # 'price_from':1,
      # 'price_to':10000,
      'dtime_from': '00:00',
      'dtime_to':'24:00',
      'atime_from': '00:00',
      'atime_to': '24:00',
      # 'stopover_from': '00:00',
      # 'stopover_to': '00:00',
      'max_stopovers': 0,
      # 'conn_on_diff_airport':1,
      # 'select_airlines': 'FR,AA',
      # 'select_airlines_exclude': False,
      # 'select_stop_airport': 'BCN,FRA',
      # 'select_stop_airport_exclude':False,
      # 'vehicle_type': 'aircraft',
      'limit': 30,
      'sort': 'price', 
      'asc': 0,
      'xml':0
    }
    json_data = get_data(url, params, headers)
    return json_normalize(json_data['data'])


#%%

def get_cheapest(from_city, from_country, to_city, to_country, start_date, end_date):
  from_fly = get_city(from_city, from_country)
  to_fly = get_city(to_city, to_country)
  flights = get_flights(from_fly, to_fly, start_date, end_date)
  flights.sort_values(by=['price'], axis=0, inplace=True)
  cheapest_price = flights.iloc[0]['price']
  return cheapest_price

result = get_cheapest('Bristol', 'UK', 'Prague', 'CZ', '19/12/2019', '24/12/2019')
print(f'Cheapest price: {result} EUR')



#%%
