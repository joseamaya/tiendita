from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout
from usuarios.views import signup

urlpatterns = patterns('',
	url(r'^registrate/$',signup, name="registrate"),
	url(r'^$', login, {'template_name': 'login.html', }, name="login"),
	url(r'^logout$', logout, {'template_name': 'logout.html', }, name="logout"),
)