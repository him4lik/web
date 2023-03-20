from django.shortcuts import render, HttpResponse, redirect, reverse
from django import views
import requests
from datetime import date
from web.settings import API_HOST
from lib.common import get_token, get_user

def get_products_categories(token=''):
	url = API_HOST+'inventory/product-category/'
	response = requests.get(url, headers={'Authorization': token})
	#validate response
	# print(response.text)
	data = response.json() #if validates
	return data

class HomePageView(views.View):
	template_name = 'product/home-page.html'

	def get(self, request):
		context = {}
		print(request.user)
		context['data'] = get_products_categories(token=request.token)
		context['user'] = request.user
		print(context)
		return render(request, self.template_name, context)

	def post(self, request):
		context = {}
		return render(request, self.template_name, context)

class ProductBrowseView(views.View):
	template_name = 'product/browse.html'
	
	def get_variants(self, params):
		url = API_HOST+'inventory/browse/'
		response = requests.get(url, params=params)
		#validate response
		data = response.json() #if validates
		return data

	def get(self, request):
		token=get_token(request)
		params ={
			'product':request.GET.get('product', None),
			'category':request.GET.get('category', None),
		}
		context = {}
		context['variants'] = self.get_variants(params)
		context['data'] = get_products_categories(token=token)
		context['user'] = get_user(token)
		print(context['variants'])
		return render(request, self.template_name, context)

	def post(self, request):
		context = {}
		return render(request, self.template_name, context) 

class ProductDetailView(views.View):
	template_name = 'product/detail.html'
	
	def get_variants(self, params):
		url = API_HOST+'inventory/browse/'
		response = requests.get(url, params=params)
		#validate response
		data = response.json() #if validates
		return data

	def get(self, request):
		token=get_token(request)
		params ={
			'product':request.GET.get('product', None),
			'category':request.GET.get('category', None),
			'title':request.GET.get('title', None),
			'parameters':request.GET.get('parameters', None)
		}
		print(params)
		context = {}
		context['variants'] = self.get_variants(params)
		context['data'] = get_products_categories(token=token)
		context['user'] = get_user(token)
		# print(context)
		return render(request, self.template_name, context)

	def post(self, request):
		context = {}
		return render(request, self.template_name, context) 