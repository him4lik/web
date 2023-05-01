from django.shortcuts import render, HttpResponse, redirect, reverse
from django import views
import requests
from web.settings import API_HOST
from lib.common import get_token, get_user
from product.forms import FilterForm
import json

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
	form = FilterForm
	
	def get_variants(self, params):
		url = API_HOST+'inventory/browse/'
		response = requests.get(url, params=params)
		#validate response
		data = response.json() #if validates
		return data

	def get(self, request):
		token=get_token(request)
		params ={
			'product':request.GET.get('product', ''),
			'category':request.GET.get('category', '')
		}
		context = {}
		data = self.get_variants(params)
		context['variants'] = data['variants']
		context['filter_opts'] = data['filter_opts']
		context['data'] = get_products_categories(token=token)
		context['user'] = get_user(token)
		choices = {}
		for parameter,values in data['filter_opts'].items():
			choices[parameter]=[]
			for val in values:
				choices[parameter].append((parameter, val))
		forms = []
		for choice, values in choices.items():
			forms.append([choice, self.form(values)])
		context['forms'] = forms
		return render(request, self.template_name, context)

	def post(self, request):
		token=get_token(request)
		params ={
			'product':request.GET.get('product', ''),
			'category':request.GET.get('category', '')
		}
		context = {}
		data = self.get_variants(params)
		context['variants'] = data['variants']
		context['filter_opts'] = data['filter_opts']
		context['data'] = get_products_categories(token=token)
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
		forms = []
		for choice, values in choices.items():
			forms.append([choice, self.form(values, {'parameter_val':([f"{choice},{i}" for i in data.get(choice, [])])})])
		context['forms']=forms
		if any([fm[1].is_valid() for fm in forms]):
			params['parameters'] = json.dumps(data)
			context['variants'] = self.get_variants(params)['variants']
			return render(request, self.template_name, context)
		else:
			print(request.POST, request.GET, context)
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
			'title':request.GET.get('title', None)
		}
		context = {}
		data = self.get_variants(params)
		context['variants'] = data['variants']
		context['filter_opts'] = data['filter_opts']
		context['data'] = get_products_categories(token=token)
		context['user'] = get_user(token)
		return render(request, self.template_name, context)

	def post(self, request):
		context = {}
		return render(request, self.template_name, context) 