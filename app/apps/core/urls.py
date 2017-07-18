from core.views import app_view
from django.conf.urls import url

urlpatterns = [
    url(r'^', app_view, name='app'),
]
