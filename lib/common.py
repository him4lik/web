import requests
from web.settings import API_HOST

def get_token(request):
	try:
		return "Bearer "+request.headers['Cookie'].split('; ')[1].split('=')[1]
	except:
		return ''

def get_refresh_token(request):
	try:
		return request.headers['Cookie'].split('; ')[2].split('=')[1]
	except:
		return ''

def get_user(token):
	url = API_HOST+'user/get-user/'
	response = requests.get(url, headers={'Authorization': token})
	print(response, response.json())
	#validate response
	# print(response.text)
	data = response.json() #if validates
	if response.status_code == 401:
		data = {**{'is_authenticated':False}, **response.json()}
	return data

def refresh_access_token(refresh_token):
	url = API_HOST+'user/get-user/'
	response = requests.get(url, headers={'Authorization': token})
	print(response, response.json())
	#validate response
	# print(response.text)
	data = response.json() #if validates
	if response.status_code == 401:
		data = {**{'is_authenticated':False}, **response.json()}
	return data