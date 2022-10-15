from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import Contacts
from .forms import ContactsForm


def show_all_contacts(request: HttpRequest) -> HttpResponse:
    contacts = Contacts.objects.all()
    return render(
        request, "contacts/index.html", {"title": "Contacts", "contacts": contacts}
    )

def generate_contacts(request: HttpRequest) -> HttpResponse:
    pass

def get_contact(request: HttpRequest, pk: int) -> HttpResponse:
    contact = Contacts.objects.get(pk=pk)
    return None
    #return render(
       # request, 'contacts/get_contact.html', {"title": "Get contact", "contact": contact}
    #)

def edit_contact(request: HttpRequest, pk: int) -> HttpResponse:
    contact = Contacts.objects.get(pk=pk)
    form = ContactsForm(instance=contact)
    return render(
        request, 'contacts/edit_contact.html',
        {
            "title": "Edit contact",
            "form": form
        }
    )

def delete_contact(request: HttpRequest) -> HttpResponse:
    pass