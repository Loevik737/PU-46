from __future__ import unicode_literals
from CheckPoint.apps.subject.models import Subject
from django.db import models
import datetime

class Plan(models.Model):
    title = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, related_name='plan')
    term = models.CharField(verbose_name='Semester', max_length=10)
    year = models.IntegerField(default=datetime.datetime.now().year)


class Week(models.Model):
    week_number = models.IntegerField(verbose_name='Ukenummer')
    plan = models.ForeignKey(Plan, related_name='weeks')


class Objectives(models.Model):
    learning_objective = models.CharField(blank=False, max_length=200)
    subject = models.ForeignKey(Subject, related_name='learning_objectives')


class Lecture(models.Model):
    date_added = models.DateField(auto_now_add=True)
    comment = models.TextField(blank=True)
    plan = models.ForeignKey(Plan, related_name='lectures')
    week = models.ForeignKey(Week, related_name='lectures')
    objectives = models.ManyToManyField(Objectives)
