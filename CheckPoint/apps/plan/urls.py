from django.conf.urls import url

from . import views

urlpatterns = [
    #sendign you to a plan if you type plan/<plan_id>(example: plan/2)
    url(r'^(?P<plan_id>[0-9]+)$', views.index, name='plan'),
    url(r'^create/$', views.create_plan, name='createPlan'),
    url(r'^addLecture/$', views.create_lecture, name='createLecture'),
]