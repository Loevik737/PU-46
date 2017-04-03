from django.conf.urls import url

from CheckPoint.apps.stats.views import student_stats_view,teacher_stats_view

urlpatterns = [
    url(r'^student$', student_stats_view, name='student_stats'),
    url(r'^teacher$', teacher_stats_view, name='teacher_stats')
]
