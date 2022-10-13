from django.db import models

from apps.contacts.typing import T_NAME


class Contacts(models.Model):
    name: T_NAME = models.CharField(max_length=20, verbose_name="Name")
    phone = models.CharField(max_length=20, verbose_name="Phone number", blank=True)
    date_of_birth = models.DateField(null=True, verbose_name="Date of birth", blank=True)

    is_auto_generated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated date")

   #class Meta:
       #verbose_name = "Contact"
       #verbose_name_plural = "Contacts"


