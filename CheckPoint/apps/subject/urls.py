from django.conf.urls import url

from CheckPoint.apps.subject.views import subjectView

urlpatterns = [
    url(r'^$', subjectView, name='home'),
]
