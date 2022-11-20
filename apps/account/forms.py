from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


from apps.users.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput)
    first_name = forms.CharField(label="Firs name", widget=forms.TextInput, required=False)
    last_name = forms.CharField(label="Last name", widget=forms.TextInput, required=False)
    email = forms.EmailField(label="Email", widget=forms.EmailInput())
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput())
    avatar = forms.ImageField(label="Avatar", required=False)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "avatar")