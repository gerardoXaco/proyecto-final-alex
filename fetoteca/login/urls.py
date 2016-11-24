from django.conf.urls import url
from login.views import login_usuario
from django.contrib.auth.views import login, logout_then_login

urlpatterns = [
	#url(r'^$', login_usuario,name="login_usuario"),
	url(r'^$', login, {'template_name':'login.html'}, name="login_usuario"),
	url(r'^cerrar/$', logout_then_login, name="logout_usuario"),
]