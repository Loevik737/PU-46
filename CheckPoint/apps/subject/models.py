from django.db import models

from django.contrib.auth.models import User
from CheckPoint.apps.registration.models import CustomUser

class Subject(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(CustomUser, limit_choices_to={'role': 'Teacher'}, related_name='subjectTeacher', null=True)

    def __str__(self):
       return 'Subject code: ' + self.code
