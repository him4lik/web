from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio

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
		print(event['text'])
		await self.send({
			'type':'websocket.send',
			'text': event['text']
			})
		# for i in range(20):
		# 	await self.send({
		# 		'type':'websocket.send',
		# 		'text':str(i)
		# 		})
		# 	await asyncio.sleep(1)

	async def websocket_disconnect(self, event):
		print('websocket disconnected')
		raise StopConsumer()