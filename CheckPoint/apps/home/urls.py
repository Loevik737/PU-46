from django.conf.urls import url

from CheckPoint.apps.home.views import homeView
#the url paths that sends you to the views you want
urlpatterns = [
    url(r'^$', homeView.as_view(), name='home'),
]
