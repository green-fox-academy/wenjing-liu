
#%%
import json
from flask import Flask, render_template
import math
import requests
import pandas as pd
import numpy as np
from sklearn import preprocessing, naive_bayes
from sklearn.model_selection import cross_val_predict, train_test_split
import os

def read_json_data():
  return pd.read_json('property_listings.json', orient='split')

# all data's listing_status = 'sale'
# all data's location_is_approximate = 0
# 5336 items missing 'letting_fees'
# 'price_change_summary', we have price_change attr
# 'displayable_address',  'street_name', 'post_town', 
# current not use 'price_modifier', 'short_description','description', 'agent_name', 'first_published_date', 'status', 'county', 'listing_id'
useful_feature = ['outcode', 'latitude', 'longitude', 'property_type','new_home',  'num_bathrooms', 'num_bedrooms', 'num_floors', 'num_recepts',  'price',  'last_published_date', 'price_change']
def clean_data(data):
  indexNames = data[data['price'] == 0].index
  data.drop(indexNames, inplace=True)
  return data

def predict_property_type(data):
  features = ['property_type','new_home',  'num_bathrooms', 'num_bedrooms', 'num_floors', 'num_recepts', 'price']
  train_data = data[data['property_type'] != ''][features]

  test_data = data[data['property_type']==''][features]
  # Get xs and y
  train_xs_data = train_data.drop('property_type', axis=1)
  train_target = train_data['property_type']
  X_train, X_test, y_train, y_test = train_test_split(train_xs_data, train_target, test_size=0.2, random_state=0)
  gnb = naive_bayes.GaussianNB()
  gnb.fit(X_train, y_train)  
  test_result = gnb.predict(test_data.drop(columns =['property_type']))
  key = ['property_type']
  for i, j in zip(key, [test_result]):
    test_data[i] = j
  data.update(test_data)
  return data


def fill_missing_value(data):
  # fill None for 'new_home' is old hourse, 0 for old, 1 for new
  data['new_home'] = data['new_home'].apply(lambda x: 0 if x==None else 1)
  # Use native bayes to fill null property_type
  data = predict_property_type(data)

  return data


def scaler_price(data):
  scaled_features = data
  col_names = ['price']
  features = scaled_features[col_names]
  scaler = preprocessing.StandardScaler().fit(features.values)
  features = scaler.transform(features.values)
  scaled_features[col_names] = features
  return scaled_features


def convert_features(data):
  # turn 'property_type' to vector
  dummies_Property_Type = pd.get_dummies(data['property_type'], prefix= 'property_type')
  
  # turn 'outcode' to vector
  # dummies_Outcode = pd.get_dummies(data['post_town'], prefix= 'post_town')

  data = pd.concat([data, dummies_Property_Type], axis=1)
  data.drop(['property_type'], axis=1, inplace=True)

  # turn 'latitude' and 'longitude' to x, y, z
  data['x'] = data.apply(lambda x: math.cos(x['latitude']) * math.cos(x['longitude']), axis=1)
  data['y'] = data.apply(lambda x: math.cos(x['latitude']) * math.sin(x['longitude']), axis=1)
  data['z'] = data.apply(lambda x: math.sin(x['latitude']), axis=1) 
  data.drop(['longitude', 'latitude'], axis=1, inplace=True)
  return data



def eda_data(data):
  raw_data = read_json_data()
  data = raw_data[useful_feature]
  eda_data = fill_missing_value(data)
  # @Claire Draw EDA figure


def get_trainning_data():
  raw_data = read_json_data()
  training_features = ['latitude', 'longitude', 'property_type','new_home',  'num_bathrooms', 'num_bedrooms', 'num_floors', 'num_recepts',  'price']
  data = raw_data[training_features]
  data = clean_data(data)
  data = fill_missing_value(data)  
  
  train_df = convert_features(data)
  return train_df

# result = get_trainning_data()
# result

#%%
