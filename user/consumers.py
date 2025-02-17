from channels.consumer import SyncConsumer, AsyncConsumer
from lib.base_classes import BaseAsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio
from web.settings import API_HOST
from lib.apis import post_as_user, get_as_user
import json
from lib.common import get_user
import requests

# class SendOTPSyncConsumer(SyncConsumer):

# 	def websocket_connect(self, event):
# 		self.send({
# 			'type': 'websocket.accept'
# 			})

# 	def websocket_receive(self, event):
# 		for i in range(20):
# 			self.send({
# 				'type':'websocket.send',
# 				'text':str(i)
# 				})
# 			sleep(1)

# 	def websocket_disconnect(self, event):
# 		raise StopConsumer()

class SendOTPAsyncConsumer(BaseAsyncConsumer):

	async def websocket_receive(self, event):
		headers = {i[0].decode():i[1].decode() for i in self.scope['headers']}
		data = json.loads(event['text'])
		decision = data.get('decision', None)
		variant_id = data.get('variant_id', None)
		url = API_HOST+'user/login-otp/'
		response = requests.get(url, params=json.loads(event['text']))
		request_id = response.json()['request_id'] #if validates
		await self.send({
			'type':'websocket.send',
			'text': json.dumps({'request_id':request_id})
			})
		return request_id
