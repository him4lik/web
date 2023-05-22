from django.urls import path
from order import consumers

ws_urlpatterns = [
	path('cart/sc/', consumers.CartSyncConsumer.as_asgi()),
	path('cart/asc/', consumers.CartAsyncConsumer.as_asgi()),
	]