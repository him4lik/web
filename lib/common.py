import requests
from web.settings import API_HOST

def get_user(token):
	url = API_HOST+'user/get-user/'
	response = requests.get(url, headers={'Authorization': f"Bearer {token}"})
	data = response.json() #if validates
	if response.status_code == 401:
		data = {**{'is_authenticated':False}, **response.json()}
	return data

def refresh_access_token(refresh_token):
	url = API_HOST+'user/get-user/'
	response = requests.get(url, headers={'Authorization': token})
	print(response, response.json())
	data = response.json() #if validates
	if response.status_code == 401:
		data = {**{'is_authenticated':False}, **response.json()}
	return data