import requests
from web.settings import API_HOST

def get_token(request):
	try:
		return "Bearer "+request.headers['Cookie'].split('; ')[1].split('=')[1]
	except:
		return ''

def get_user(token):
	url = API_HOST+'user/get-user/'
	response = requests.get(url, headers={'Authorization': token})
	#validate response
	# print(response.text)
	data = response.json() #if validates
	return data