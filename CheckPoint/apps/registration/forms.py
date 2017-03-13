from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

ROLES = (
    ('Teacher', _("Teacher")),
    ('Student', _("Student"))
)

#a form for registering a new user

class RegistrationForm(forms.Form):
    #field for username, can only include letters, numbers and underscores
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)),
                                label=_("Username"), error_messages={
            'invalid': _("This value must contain only letters, numbers and underscores.")})
    #field for email
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
    #first password field
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    #second password field
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)),
        label=_("Password (again)"))
    role = forms.ChoiceField(choices = ROLES    , widget=forms.Select(), required=True)

    def clean_role(self):
        for i,v in ROLES:
            if self.cleaned_data['role'] == i:
                return self.cleaned_data['role']
        raise forms.ValidationError("Your role must be one of the pre defined roles", code='The role was not accepted')

    #checks if the username already exists
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))

    #checks whether or not the password fields match
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data
