

from django.conf.urls import url

from . import views

#the url paths that sends you to the views you want
urlpatterns = [
    url(r'^$', views.register, name="register"),
    url(r'^success/$', views.register_success, name="register_success"),
]
