from django.contrib.auth.models import User
from django import forms

# a formclass witch we can use to change user data
class UpdateUser(forms.ModelForm):
    #creating a formfield for username
    username = forms.CharField(required=False,label='Change username',
                    widget=forms.TextInput(attrs={'placeholder': 'new username'}))
    #creating a formfield for email
    email = forms.EmailField(required=False,label='Change email',
                    widget=forms.TextInput(attrs={'placeholder': 'new email...'}))
    #creating a formfield for last name
    first_name = forms.CharField(required=False,label='Change first name',
                    widget=forms.TextInput(attrs={'placeholder': 'new first name'}))
    #creating a formdef test_role(self):field for last name
    last_name = forms.CharField(required=False,label='Change last name',
                    widget=forms.TextInput(attrs={'placeholder': 'new last name'}))
    #the model we will use will be the auth User model and the fields are named username,email
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name',)
    #checks if the email was used before
    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        return email
