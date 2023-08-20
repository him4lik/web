import requests
from web.settings import API_HOST

def get_as_user(url, params={}, token=''):
	print(params, '111111111111')
	response = requests.get(url, params=params, headers={'Authorization': token})
	data = response.json()
	return data

def post_as_user(url, data={}, token=''):
	response = requests.post(url, data=data, headers={'Authorization': f"Bearer {token}"})
	print(response.text, response)
	data = response.json()
	return data

def get_variants(params, token=''):
	url = API_HOST+'inventory/browse/'
	response = requests.get(url, params=params, headers={'Authorization': token})
	#validate response
	data = response.json() #if validates
	return data

def get_cart_items(token=''):
	url = API_HOST + 'order/cart/'
	response = requests.get(url, headers={'Authorization': token})
	data = response.json()
	return data