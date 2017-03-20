from django.db import models

from django.contrib.auth.models import User
from CheckPoint.apps.subject.models import Subject

class CostumUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=30)
    def __unicode__(self):
       return self.user.username 
