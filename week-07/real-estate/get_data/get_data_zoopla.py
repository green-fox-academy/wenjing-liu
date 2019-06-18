from flask import Flask, render_template
import requests
import pandas as pd

API_URL='https://api.zoopla.co.uk/api/v1/'
api_key='9dud55d9tr4ptf7umqt4rmf6'


def property_listings():
	page_number = 1
	page_size = 100
	params = {
		'page_number': page_number,
		'page_size': page_size,
		'listing_status': 'sale',
		'include_sold': 1,
		'area': 'Somerset'
	}

	params.update({'api_key': api_key})
	action = 'property_listings.json'
	response = requests.get(API_URL + action, params)
	data = []
	print(response)
	if response.ok:
		raw_data = response.json()
		data.extend(raw_data['listing'])
		while (len(data) < int(raw_data['result_count'])):
			print(len(data))
			page_number += 1
			params.update({'page_number': page_number})
			response = requests.get(API_URL + action, params)
			raw_data = response.json()
			data.extend(raw_data['listing'])
		print(len(data))
		df = pd.DataFrame(data)
		print()
		df.to_json('property_listings.json', orient='split')

property_listings()