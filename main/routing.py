from django.urls import re_path

from observation import consumers

websocket_urlpatterns = [
    re_path(r'ws/status/', consumers.StatusConsumer),
]