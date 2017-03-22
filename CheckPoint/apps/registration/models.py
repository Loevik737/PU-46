from django.db import models

from django.contrib.auth.models import User

class CostumUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=30)
    attendingSubject = models.ManyToManyField('subject.Subject',related_name="attend_subject")
    def __unicode__(self):
       return self.user.username
