from django import forms
from django.contrib.auth.models import User
from fdtusers.models import amUserProfileInfo


class amUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class amUserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = amUserProfileInfo
        fields = ('portfolio_site','profile_pic')
