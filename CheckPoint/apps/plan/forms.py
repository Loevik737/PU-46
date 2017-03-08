from .models import Plan, Lecture, Week
from django import forms
from django.forms import ModelForm
from CheckPoint.apps.subject.models import Subject
from django.forms import ModelChoiceField
import datetime
from django.core.validators import MinValueValidator, MaxValueValidator

#a costum ModelChoiceField class so we can get the name of the
#subject in the dropdown menu in CreatePlan form
class SubjectModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
         return obj.name

# a formclass witch we can use to create a new plan
class CreatePlan(ModelForm):
    #creating a textfield for title
    title = forms.CharField(required=True,label='Title',
                    widget=forms.TextInput(attrs={'placeholder': 'title...'}))
    #creating a dropdown for subjects witch gets all the subjects from the database
    subject = SubjectModelChoiceField(queryset = Subject.objects.all())
    #creating a textfield for term
    term = forms.CharField(required=True,label='Term:',
                    widget=forms.TextInput(attrs={'placeholder': 'term...'}))
    #creating a IntegerField for the year, the default is the current year
    year = forms.IntegerField(required=True,label='Year:',initial=datetime.datetime.now().year)

    #the model we will use will be the auth User model and the fields are named title, subject, term, year
    class Meta:
        model = Plan
        fields = ('title','subject','term','year')


class CreateLectureForm(ModelForm):
    objectives_form_field = forms.CharField(label='Learning objectives',
                                            widget=forms.TextInput(attrs={
                                                'placeholder': "Learningobjectives seperated by ';'"}
                                            ))
    class Meta:
        model = Lecture
        exclude = ['plan','week', 'objectives']
        fields = ['title', 'comment']

class DeleteLectureForm(ModelForm):
    class Meta:
        model =  Lecture
        fields = []

class CreateWeekForm(ModelForm):
    class Meta:
        model = Week
        exclude = ['plan', 'week_number']

class DeleteWeekForm(ModelForm):
    class Meta:
        model = Week
        fields = []
