from django.shortcuts import render, HttpResponse, redirect, reverse
from django import views
from user import forms
import requests
from web.settings import API_HOST
from product.views import get_products_categories

class CartView(views.View):
	template_name = 'order/cart.html'
	redirect_url = 'login'

	def get(self, request):
		if not request.user['is_authenticated']:
			return redirect(reverse(self.redirect_url))
		context = {}
		context['user'] = request.user
		context['data'] = get_products_categories(token=request.token)
		return render(request, self.template_name, context)

	def post(self, request):
		context = {}
		return render(request, self.template_name, context)