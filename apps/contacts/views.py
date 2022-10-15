from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import Contacts
from .forms import ContactsForm, UserForm


def show_all_contacts(request: HttpRequest) -> HttpResponse:
    contacts = Contacts.objects.all()
    return render(
        request, "contacts/index.html", {"title": "Contacts", "contacts": contacts}
    )

def create_contact(request: HttpRequest) -> HttpResponse:
    form = UserForm()
    context = {'form': form}
    return render(request, "contacts/create_contact.html", context)

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
        request, 'contacts/edit_form.html',
        {
            "title": "Edit contact",
            "form": form
        }
    )

def delete_contact(request: HttpRequest) -> HttpResponse:
    pass