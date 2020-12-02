from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . models import User
from django.forms.widgets import PasswordInput, EmailInput, TextInput

text_classes = "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
password_classes = "shadow appearance-none border border-red-500 rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"


class UserCreateForm(UserCreationForm):
    email = forms.CharField(widget=EmailInput(attrs={ 'class': text_classes, 'placeholder': 'Email', 'id': 'email' }))
    password = forms.CharField(
        widget=PasswordInput(attrs={ 'class': password_classes, 'placeholder': 'Password', 'id': "password" }))
    password2 = forms.CharField(
        widget=PasswordInput(attrs={ 'class': password_classes, 'placeholder': 'Password', 'id': "password2" }))
    first_name = forms.CharField(widget=TextInput(attrs={'class': text_classes, 'id': 'first_name', 'placeholder': 'First Name'}))
    last_name = forms.CharField(
        widget=TextInput(attrs={ 'class': text_classes, 'id': 'last_name', 'placeholder': 'Last Name' }))
    username = forms.CharField(
        widget=TextInput(attrs={ 'class': text_classes, 'id': 'username', 'placeholder': 'Username' }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')



class CustomLoginForm(AuthenticationForm):
    email = forms.CharField(widget=EmailInput(attrs={'class':text_classes,'placeholder': 'Email', 'id': 'email'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': password_classes,'placeholder':'Password',  'id':"password"}))

