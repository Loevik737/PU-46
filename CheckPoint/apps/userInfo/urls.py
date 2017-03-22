from django.conf.urls import url

from . import views

#the url paths that sends you to the views you want
urlpatterns = [
    url(r'^$', views.index, name='userIndex'),
    url(r'^edit/$',views.user_info,name='editUser')
]
