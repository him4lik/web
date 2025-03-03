from django.urls import path, include
from order import consumers
from channels.routing import URLRouter
import product.routing
import order.routing
import user.routing

ws_urlpatterns = [
	*product.routing.ws_urlpatterns,
	*order.routing.ws_urlpatterns,
	*user.routing.ws_urlpatterns
	]