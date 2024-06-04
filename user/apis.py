def send_otp(phone):
	url = API_HOST+'user/login-otp/'
	response = requests.get(url, params={'phone':phone})
	#validate response
	request_id = response.json()['request_id'] #if validates
	return request_id

def validate_otp(request_id, otp):
	url = API_HOST+'user/login-otp/'
	response = requests.post(url, data={'request_id':request_id, 'otp':otp})
	#validate response
	tokens = {
		'access':response.json()['access'],
		'refresh':response.json()['refresh']
	}
	return tokens #based on validation
