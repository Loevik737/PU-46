from django.conf.urls import url

from CheckPoint.apps.stats.views import stats_view

urlpatterns = [
    url(r'^$', stats_view, name='stats'),
]
