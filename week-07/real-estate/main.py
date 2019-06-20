from flask import Flask, render_template, redirect, url_for, request
import joblib
import json
import pandas as pd
import math
import postcodes_io_api
import requests
from get_data import convert_features, convert_lat_log
app = Flask(__name__)

property_types = ['Barn conversion', 'Block of flats', 'Bungalow', 'Chalet', 'Cottage', 'Country house', 'Detached bungalow', 'Detached house', 'End terrace house', 'Equestrian property', 'Farm', 'Farmhouse', 'Flat', 'Hotel/guest house', 'Houseboat', 'Land', 'Link-detached house', 'Lodge', 'Maisonette', 'Mews house', 'Mobile/park home', 'Parking/garage', 'Semi-detached bungalow', 'Semi-detached house', 'Studio', 'Terraced bungalow', 'Terraced house', 'Town house', 'Villa']


def get_lat_log(postcode):
  api  = postcodes_io_api.Api(debug_http=True)
  data = api.get_postcode(postcode)
  return [data['result']['longitude'], data['result']['latitude']]


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/estimate', methods=['POST'])
def estimate():
  property = { 
    'post_code': request.form['post_code'],
    'new_home': request.form['new_home'],
    'property_type': request.form['property_type'],
    'num_bedrooms': request.form['num_bedrooms'],
    'num_bathrooms': request.form['num_bathrooms'],
    'num_floors': request.form['num_floors'],
    'num_recepts': request.form['num_recepts']
  }
  [longitude, latitude] = get_lat_log(property['post_code'])
  property['latitude'] = latitude
  property['longitude'] = longitude

  for type in property_types:
    property['property_type_' + type] = 1 if type == property['property_type'] else 0
  data = [property]
  df = pd.DataFrame(data)
  df.drop(columns=['post_code', 'property_type'], inplace=True)
  converted_df = convert_lat_log(df)
  loaded_model = joblib.load('./get_data/finalized_model.sav')
  result = loaded_model.predict(converted_df)
  return render_template('result.html', property=property, result=int(result[0]))
