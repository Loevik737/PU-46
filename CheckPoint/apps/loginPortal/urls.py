from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView


urlpatterns = [
    url(r'^$', auth_views.login, {'template_name': 'myApp/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login' }, name='logout'),
]
