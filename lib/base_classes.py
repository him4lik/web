from django import views
from django.shortcuts import render, HttpResponse, redirect, reverse

class View(views.View):
	context = {}
	forms = [] 

class BaseView(views.View):

	def get_context_data(self, request):
		token = request.token
		context = {}
		forms = []

	def post_context_data(self, request):
		token = request.token
		context = {}
		forms = []

	def get(self, request):
		context = self.get_context_data(request)
		return render(request, self.template_name, context)

	def post(self, request):
		context = self.post_context_data(request)
		return render(request, self.template_name, context) 