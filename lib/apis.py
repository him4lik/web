import requests
from web.settings import API_HOST

def get_as_user(url, params={}, headers={}):
	print(params, '111111111111')
	response = requests.get(url, params=params, headers=headers)
	data = response.json()
	return data

def post_as_user(url, data={}, headers={}):
	response = requests.post(url, data=data, headers=headers)
	print(response.text, response)
	data = response.json()
	return data

def get_variants(params, headers={}):
	url = API_HOST+'inventory/browse/'
	response = requests.get(url, params=params, headers=headers)
	#validate response
	data = response.json() #if validates
	return data

def get_cart_items(headers={}):
	url = API_HOST + 'order/cart/'
	response = requests.get(url, headers=headers)
	data = response.json()
	return data