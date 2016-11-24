from django.conf.urls import url
from foro.views import foro

urlpatterns = [
	url(r'^', foro, name='foro'),
]