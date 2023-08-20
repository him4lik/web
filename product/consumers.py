from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio
from web.settings import API_HOST
from lib.apis import post_as_user, get_as_user
import json
from lib.common import get_user

class AddToCartSyncConsumer(SyncConsumer):

	def websocket_connect(self, event):
		print('websocket connected')
		self.send({
			'type': 'websocket.accept'
			})

	def websocket_receive(self, event):
		print('websocket received')
		print(event['text'])
		for i in range(20):
			self.send({
				'type':'websocket.send',
				'text':str(i)
				})
			sleep(1)

	def websocket_disconnect(self, event):
		print('websocket disconnected')
		raise StopConsumer()

class AddToCartAsyncConsumer(AsyncConsumer):

	async def websocket_connect(self, event):
		print('websocket connected')
		await self.send({
			'type': 'websocket.accept'
			})

	async def websocket_receive(self, event):
		print('websocket received')
		print(event['text'],type(event['text']), ({i[0].decode():i[1].decode() for i in self.scope['headers']}))
		headers = {i[0].decode():i[1].decode() for i in self.scope['headers']}
		print(headers)
		token = headers['cookie'].split('; ')[1].split('=')[1]
		await self.send({
			'type':'websocket.send',
			'text': event['text']
			})
		data = json.loads(event['text'])
		decision = data.get('decision', None)
		variant_id = data.get('variant_id', None)
		print(API_HOST+'order/cart/', token, data)
		print(get_user(token))
		data = post_as_user(
			API_HOST+'order/cart/',
			data=data,
			token=token)
		print(data)

	async def websocket_disconnect(self, event):
		print('websocket disconnected')
		raise StopConsumer()

class ProductFilterAsyncConsumer(AsyncConsumer):

	async def websocket_connect(self, event):
		print('websocket connected')
		await self.send({
			'type': 'websocket.accept'
			})

	async def websocket_receive(self, event):
		print('websocket received')
		print(event['text'], ({i[0].decode():i[1].decode() for i in self.scope['headers']}))
		headers = {i[0].decode():i[1].decode() for i in self.scope['headers']}
		print(headers)
		token = headers['cookie'].split('; ')
		if len(token)!=1:
			token = token[1].split('=')[1]
		else:
			token = ''
		params = json.loads(event['text'])
		params["parameters"] = json.dumps(params["parameters"])

		print(API_HOST+'inventory/browse/', token, params)
		print(get_user(token))
		data = get_as_user(
			API_HOST+'inventory/browse/',
			params=params,
			token=token)
		print(data)
		await self.send({
			'type':'websocket.send',
			'text': json.dumps(data),
			})

	async def websocket_disconnect(self, event):
		print('websocket disconnected')
		raise StopConsumer()