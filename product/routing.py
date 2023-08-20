from django.urls import path
from product import consumers

ws_urlpatterns = [
	path('sc/product/add-to-cart/', consumers.AddToCartSyncConsumer.as_asgi()),
	path('ac/product/add-to-cart/', consumers.AddToCartAsyncConsumer.as_asgi()),
	path('ac/product/filter/', consumers.ProductFilterAsyncConsumer.as_asgi()),
	]