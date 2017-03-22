from __future__ import unicode_literals

import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from multiselectfield import MultiSelectField

from CheckPoint.apps.registration.models import CostumUser
from CheckPoint.apps.subject.models import Subject

#choises that can be taken, (number(as an id), Text for the choice)
MY_CHOICES = (('item_key1', 'Choice 0'),
              ('item_key2', 'Choice 1'),
              ('item_key3', 'Choice 2'),
              ('item_key4', 'Choice 3'))

class Assignment(models.Model):
    title = models.CharField(max_length=500)
    subject = models.ForeignKey(Subject, related_name='Assignment')
    term = models.CharField(verbose_name='Semester', max_length=10)
    year = models.IntegerField(default=datetime.datetime.now().year)
    tries = models.IntegerField(default=3)
    due = models.DateField(default =datetime.datetime.now(), blank=True)

#pip install django-multiselectfield
class MultipleChoiseQuestion(models.Model):
    question = models.CharField(max_length=500)
    #importing MultiSelectField and using the choises as defined earlier
    choises = MultiSelectField(choices=MY_CHOICES,
                                 max_choices=4)
    answear = models.IntegerField(default= 0,validators=[MinValueValidator(0), MaxValueValidator(3)])
    assignment = models.ForeignKey(Assignment, related_name='MultipleChoiseQuestions')

#the TrueFalseQuestion and OneWordQuestion classes  are normal model clases with nothing new to comment
class TrueFalseQuestion(models.Model):
    question = models.CharField(max_length=200)
    answear = models.BooleanField(default=False)
    assignment = models.ForeignKey(Assignment, related_name='TrueFalseQuestions')

class OneWordQuestion(models.Model):
    question = models.CharField(max_length=500)
    answear = models.CharField(max_length=100)
    assignment = models.ForeignKey(Assignment, related_name='OneWordQuestions')

class UserAnswers(models.Model):
    user = models.ForeignKey(CostumUser)
    assignment = models.ForeignKey(Assignment,related_name="UserAnswers")
    attempts = models.IntegerField(default= 0)
    wrongTFQ = models.ManyToManyField(TrueFalseQuestion)
    wrongOWQ = models.ManyToManyField(OneWordQuestion)
    wrongMCQ = models.ManyToManyField(MultipleChoiseQuestion)
