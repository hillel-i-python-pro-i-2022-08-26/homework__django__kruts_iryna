from django import forms
from django.forms import SelectDateWidget

from apps.contacts.models import Contacts


class ContactsForm(forms.ModelForm):
    date = forms.DateField(widget=SelectDateWidget())

    class Meta:
        model = Contacts
        fields = "__all__"