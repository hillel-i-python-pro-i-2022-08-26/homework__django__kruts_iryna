from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import Contacts


def show_all_contacts(request: HttpRequest) -> HttpResponse:
    contacts = Contacts.odjects.all()
    return render(
        request, "contact/index.html", {"title": "Contacts", "contacts": contacts}
    )
