from django.conf.urls import url

from . import views

urlpatterns = [
    #sendign you to a plan if you type plan/<plan_id>(example: plan/2)
    url(r'^(?P<assignment_id>[0-9]+)$', views.index, name='assignment'),
    url(r'^(?P<assignment_id>[0-9]+)/answer$',views.answer_assignment, name = "answer"),
    url(r'^(?P<assignment_id>[0-9]+)/edit$', views.edit_assignment, name='editAssignment'),
    url(r'^(?P<assignment_id>[0-9]+)/result$', views.result_assignment, name='resultAssignment'),
    url(r'^create/$', views.create_assignment, name = "create"),
    url(r'all/$', views.viewSubjectAssignments, name = "all")
]
