from core import views
from django.conf.urls import include
from django.conf.urls import url
from django.conf import settings

api_patterns = [
    url(r'^teste/?$', views.teste_api, name='teste'),
]

urlpatterns = [
    url(r'^api/v%s/' % settings.API_VERSION,
        include(api_patterns, namespace='api')),
    url(r'^(?!api|ws)', views.app_view, name='app'),
]
