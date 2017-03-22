from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from CheckPoint.apps.home.views import homeView

urlpatterns = [
    url(r'^$', auth_views.login, {'template_name': 'myApp/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'myApp/logged_out.html'}, name='logout'),
]
