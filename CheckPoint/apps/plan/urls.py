from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<plan_id>[0-9]+)$', views.index, name='plan'),
]