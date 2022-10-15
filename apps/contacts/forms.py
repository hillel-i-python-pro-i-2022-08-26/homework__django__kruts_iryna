from django import forms
from django.forms import SelectDateWidget
from django.forms import ModelForm
from .models import Contacts

from apps.contacts.models import Contacts


class UserForm(ModelForm):
    class Meta:
        model = Contacts
        fields = "__all__"


class ContactsForm(forms.ModelForm):
    date = forms.DateField(widget=SelectDateWidget())

    class Meta:
        model = Contacts
        fields = "__all__"