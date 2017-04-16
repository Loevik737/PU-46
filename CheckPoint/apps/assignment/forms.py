from CheckPoint.apps.assignment.models import Assignment, MultipleChoiseQuestion,TrueFalseQuestion,OneWordQuestion
import datetime
from django import forms
from django.forms import ModelChoiceField
from CheckPoint.apps.subject.models import Subject


#a costum ModelChoiceField class so we can get the name of the
#subject in the dropdown menu in CreatePlan form
class SubjectModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
         return obj.name

# a formclass witch we can use to create a new plan
class CreateAssignment(forms.ModelForm):
    #creating a textfield for title
    title = forms.CharField(required = True,label='Title:',
                    widget=forms.TextInput(attrs={'placeholder': 'title...','class':'form-control'}))
    #creating a dropdown for subjects witch gets all the subjects from the database
    subject = SubjectModelChoiceField(queryset = Subject.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    #creating a textfield for term
    term = forms.CharField(required = True,label='Term:',
                    widget=forms.TextInput(attrs={'placeholder': 'term...','class':'form-control'}))
    #creating a IntegerField for the year, the default is the current year
    year = forms.IntegerField(required = True,label='Year:',initial=datetime.datetime.now().year,
                    widget=forms.NumberInput(attrs={'class':'form-control'}))
    tries = forms.IntegerField(required = True, label='Tries:',initial=3,
                    widget=forms.NumberInput(attrs={'class':'form-control'}))
    #the model we will use will be the auth User model and the fields are named title, subject, term, year
    class Meta:
        model = Assignment
        fields = ('title','subject','term','year','tries')

class CreateMultipleChoiseQuestion(forms.ModelForm):
    #this is wmpty so we just use the fields from the model,
    #the reason is complications with fields for multiple choises
    class Meta:
        model = MultipleChoiseQuestion
        fields = ('question','answear','choises')

class CreateTrueFalseQuestion(forms.ModelForm):
    question = forms.CharField(required=True,label="Question:",
                    widget=forms.TextInput(attrs={'placeholder': 'questin...','class':'form-control'}))
    answear = forms.BooleanField(required=False, initial=False, label='True?:')

    class Meta:
        model = TrueFalseQuestion
        fields = ('question','answear')

class CreateOneWordQuestion(forms.ModelForm):
    question = forms.CharField(required=True,label="Question:",
                    widget=forms.TextInput(attrs={'placeholder': 'questin...','class':'form-control'}))
    answear = forms.CharField(required=True,label="Answer:",
                    widget=forms.TextInput(attrs={'placeholder': 'answer...','class':'form-control'}))
    #a costum validation for checking if the answear contains spaces
    def clean_answear(self):
        answear = self.cleaned_data['answear']
        if ' ' in answear:
            raise forms.ValidationError("answear can't containg spaces", code='contained space')
        return answear

    class Meta:
        model = OneWordQuestion
        fields = ('question','answear')
