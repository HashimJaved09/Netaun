from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class CustomUserCreationForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = False
        self.fields['email'].label = False
        self.fields['password1'].label = False
        self.fields['password2'].label = False

        self.fields['username'].icon_name = 'star'

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username', 'class': 'form-control fa fa-star-o'}), min_length=4, max_length=150)
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'confirm password'}))

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user