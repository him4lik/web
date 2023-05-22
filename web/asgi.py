import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import web.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web.settings')

application = ProtocolTypeRouter({
	'http': get_asgi_application(),
	'websocket':URLRouter(
		web.routing.ws_urlpatterns
		)
	})
