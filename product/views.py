from django.shortcuts import render, HttpResponse, redirect, reverse
from django import views
import requests
from web.settings import API_HOST
from lib.common import get_user
from product.forms import FilterForm
import json
from lib.apis import (
	get_as_user, 
	get_variants
)
from lib.base_classes import BaseView

def get_products_categories(headers):
	url = API_HOST+'product-category/'
	response = requests.get(url, headers=headers)
	#validate response
	# print(response.text)
	data = response.json() #if validates
	return data

class HomePageView(views.View):
	template_name = 'home-page.html'

	def get(self, request):
		print(request.user)
		context = {}
		context['data'] = get_as_user(
			API_HOST+'inventory/product-category/',
			headers = request.api_headers)
		context['user'] = request.user
		print(context)
		return render(request, self.template_name, context)

	def post(self, request):
		context = {}
		return render(request, self.template_name, context)

class ProductBrowseView(BaseView):
	template_name = 'browse.html'
	form = FilterForm

	def get_context_data(self, request):
		token = request.token
		context = {}
		forms = []
		#get_variants
		params ={
			'product':request.GET.get('product', ''),
			'category':request.GET.get('category', '')
		}
		variants = get_variants(params, request.api_headers)
		print(variants)
		#get_product_vategories
		products_categories = get_products_categories(headers=request.api_headers)
		
		#get_forms_data
		choices = {}
		for parameter,values in variants['filter_opts'].items():
			choices[parameter]=[]
			for val in values:
				choices[parameter].append((parameter, val))
		for choice, values in choices.items():
			forms.append([choice, self.form(values)])

		filters = []
		for choice, values in choices.items():
			filters.append([choice, values])

		#context
		context['variants'] = variants['variants']
		print(context['variants'])
		context['filter_opts'] = variants['filter_opts']
		context['data'] = products_categories
		context['user'] = request.user
		context['forms'] = forms
		context['product'] = request.GET.get('product', '')
		context['category'] = request.GET.get('category', '')
		context['filters'] = filters

		return context

	def post_context_data(self, request):
		token = request.token
		context = {}
		forms = []
		params ={
			'product':request.GET.get('product', ''),
			'category':request.GET.get('category', '')
		}
		data = get_variants(params, request.api_headers)
		context['variants'] = data['variants']
		context['filter_opts'] = data['filter_opts']
		context['data'] = get_products_categories(headers=request.api_headers)
		context['user'] = get_user(token)
		choices = {}
		for parameter,values in data['filter_opts'].items():
			choices[parameter]=[]
			for val in values:
				choices[parameter].append((parameter, val))
		d=dict(request.POST)
		req=request.POST.getlist('parameter_val')
		data = {}
		for i in req:
			dt=i.split(',')
			try:
				data[dt[0]].append(dt[1])
			except:
				data[dt[0]]=[dt[1]]
		choices = {}
		for parameter,values in context['filter_opts'].items():
			choices[parameter]=[]
			for val in values:
				choices[parameter].append((parameter, val))
		for choice, values in choices.items():
			forms.append([choice, self.form(values, {'parameter_val':([f"{choice},{i}" for i in data.get(choice, [])])})])
		context['forms']=forms
		if any([fm[1].is_valid() for fm in forms]):
			params['parameters'] = json.dumps(data)
			context['variants'] = get_variants(params, request.api_headers)['variants']
		context['product'] = request.GET.get('product', '')
		context['category'] = request.GET.get('category', '')
		return context

class ProductDetailView(views.View):
	template_name = 'detail.html'
	
	def get_variants(self, params, headers):
		url = API_HOST+'inventory/browse/'
		response = requests.get(url, params=params, headers=headers)
		#validate response
		data = response.json() #if validates
		return data

	def get(self, request):
		token = request.token
		params ={
			'product':request.GET.get('product', None),
			'category':request.GET.get('category', None),
			'title':request.GET.get('title', None)
		}
		context = {}
		data = self.get_variants(params, request.api_headers)
		context['variants'] = data['variants']
		context['filter_opts'] = data['filter_opts']
		context['data'] = get_products_categories(headers=request.api_headers)
		context['user'] = get_user(token)
		return render(request, self.template_name, context)

	def post(self, request):
		context = {}
		return render(request, self.template_name, context) 