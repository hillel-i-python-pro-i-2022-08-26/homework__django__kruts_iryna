from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from .models import Contacts
from .forms import ContactsForm, UserForm


def show_all_contacts(request: HttpRequest) -> HttpResponse:
    contacts = Contacts.objects.all()
    return render(
        request, "contacts/index.html", {"title": "Contacts", "contacts": contacts}
    )
#https://www.youtube.com/watch?v=EX6Tt-ZW0so
def create_contact(request: HttpRequest) -> HttpResponse:
    form = UserForm()
    if request.method == 'POST':
        #print("Printing POST:", request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, "contacts/create_contact.html", context)

def get_contact(request: HttpRequest, pk: int) -> HttpResponse:
    contact = Contacts.objects.get(pk=pk)
    return None
    #return render(
       # request, 'contacts/get_contact.html', {"title": "Get contact", "contact": contact}
    #)

def edit_contact(request: HttpRequest, pk:int) -> HttpResponse:
    contact = Contacts.objects.get(pk=pk)
    form = ContactsForm(instance=contact)
    return render(
        request, 'contacts/edit_form.html',
        {
            "title": "Edit contact",
            "form": form
        }
    )

def delete_contact(request: HttpRequest, pk) -> HttpResponse:
    contact = Contacts.objects.get(pk=pk)
    context = {'item': contact}
    return render(request, 'contact/delete_contact.html', context)

