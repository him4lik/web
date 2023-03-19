from django.shortcuts import render, HttpResponse, redirect, reverse
from django import views
from user import forms
import requests
from web.settings import API_HOST

class LoginView(views.View):
	template_name = 'user/login-page.html'
	form = forms.LoginForm
	redirect_url = 'otp-page'

	def send_otp(self, phone):
		url = API_HOST+'user/login-otp/'
		response = requests.get(url, params={'phone':phone})
		#validate response
		request_id = response.json()['request_id'] #if validates
		return request_id
	
	def get(self, request):
		fm = self.form()
		context = {'form':fm}
		return render(request, self.template_name, context)

	def post(self, request):
		fm = self.form(request.POST)
		context = {'form':fm}
		if fm.is_valid():
			request_id = self.send_otp(request.POST['phone'])
			return redirect(reverse(self.redirect_url) + f"?request_id={request_id}") 
		else:
			return render(request, self.template_name, context)

class OTPView(views.View):
	template_name = 'user/otp-page.html'
	form = forms.OTPForm
	redirect_url = 'home'

	def validate_otp(self, request_id, otp):
		url = API_HOST+'user/login-otp/'
		response = requests.post(url, data={'request_id':request_id, 'otp':otp})
		#validate response
		return response.json()['access'] #based on validation

	def get(self, request):
		fm = self.form(initial={'request_id':request.GET['request_id']}) #populate request id
		context = {'form':fm}
		return render(request, self.template_name, context)

	def post(self, request):
		fm = self.form(request.POST)
		context = {'form':fm}
		if fm.is_valid():
			token = self.validate_otp(request.POST['request_id'], request.POST['otp'])
			response = redirect(reverse(self.redirect_url))
			response.set_cookie('bearer', token, httponly=True)#, secure=True)
			return response
		else:
			return render(request, self.template_name, context) 

class LogoutView(views.View):
	redirect_url = 'home'
	
	def get(self, request):
		response = redirect(reverse(self.redirect_url))
		response.delete_cookie('bearer')#, secure=True)
		return response