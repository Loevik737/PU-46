from django.conf.urls import url

from . import views

urlpatterns = [
    #sendign you to a plan if you type plan/<plan_id>(example: plan/2)
    url(r'^(?P<plan_id>[0-9]+)$', views.index, name='plan'),
    url(r'^create/$', views.create_plan, name='createPlan'),
    url(r'^addLecture/$', views.create_or_edit_lecture, name='createLecture'),
    url(r'editLecture/$', views.create_or_edit_lecture, name='editLecture'),
    url(r'^deleteLecture/$', views.delete_lecture, name='deleteLecture'),
    url(r'^(?P<plan_id>[0-9]+)/createWeek/$', views.create_week, name='createWeek'),
    url(r'^deleteWeek/$', views.delete_week, name='deleteWeek'),
]