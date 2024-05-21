from django.shortcuts import render, HttpResponse, redirect, reverse
from django import views
from lib.base_classes import View
from user import forms
import requests
from web.settings import API_HOST
from product.views import get_products_categories
from lib.apis import get_cart_items
from lib.decorators import login_required
# from django.contrib.auth.decorators import login_required

class CartView(View):
	template_name = 'order/cart.html'
	redirect_url = 'login'

	@login_required
	def get(self, request):
		self.context['user'] = request.user
		self.context['data'] = get_products_categories(headers=request.api_headers)
		self.context['cart_items'] = get_cart_items(headers=request.api_headers)
		print(self.context)
		return render(request, self.template_name, self.context)

	@login_required
	def post(self, request):
		context = {}
		return render(request, self.template_name, context)