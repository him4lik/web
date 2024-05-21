from django.urls import path
from user import consumers

ws_urlpatterns = [
	# path('sc/user/send-otp/', consumers.SendOTPSyncConsumer.as_asgi()),
	path('ac/user/send-otp/', consumers.SendOTPAsyncConsumer.as_asgi()),
	]