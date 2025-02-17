from django import views
from channels.consumer import SyncConsumer, AsyncConsumer
from django.shortcuts import render, HttpResponse, redirect, reverse
from channels.exceptions import StopConsumer


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

class BaseAsyncConsumer(AsyncConsumer):
	async def websocket_connect(self, event):
		await self.send({
			'type': 'websocket.accept'
			})

	async def websocket_disconnect(self, event):
		raise StopConsumer()
