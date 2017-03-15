from django.db import models

from django.contrib.auth.models import User

class Subject(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(User, related_name='subjectTeacher',null=True)
