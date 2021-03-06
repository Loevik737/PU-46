from django.db import models
from django.contrib.auth.models import User
#from CheckPoint.apps.subject.models import Subject


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=30)
    attendingSubject = models.ManyToManyField('subject.Subject',related_name="attend_subject")
    teachingSubject = models.ManyToManyField('subject.Subject',related_name="teaching_subject")

    def __str__(self):
       return self.user.username
