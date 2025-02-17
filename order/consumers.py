from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio

class CartSyncConsumer(SyncConsumer):

	def websocket_connect(self, event):
		self.send({
			'type': 'websocket.accept'
			})

	def websocket_receive(self, event):
		for i in range(20):
			self.send({
				'type':'websocket.send',
				'text':str(i)
				})
			sleep(1)

	def websocket_disconnect(self, event):
		raise StopConsumer()

class CartAsyncConsumer(AsyncConsumer):

	async def websocket_connect(self, event):
		await self.send({
			'type': 'websocket.accept'
			})

	async def websocket_receive(self, event):
		print('websocket received')
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
		raise StopConsumer()