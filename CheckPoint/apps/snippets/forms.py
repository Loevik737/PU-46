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
    #teh model we wil use wil be the auth User modelm and the fields are named username,email
    class Meta:
        model = User
        fields = ('username', 'email')
    #checks if the email was used before
    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        return email
