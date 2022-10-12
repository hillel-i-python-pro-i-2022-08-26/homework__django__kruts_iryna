from django.db import models

class Contacts(models.Model):
    name = models.CharField(max_length=20, verbose_name="Name")
    phone = models.CharField(max_length=20, verbose_name="Phone number")
    date_of_birth = models.DateField(null=True, verbose_name="Date of birth")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated date")

   class Meta:
       verbose_name = "Contact"
       verbose_name_plural = "Contacts"


