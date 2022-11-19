from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView, CreateView, DeleteView

from .models import Contacts


class ArticleListView(ListView):
    model = Contacts


class ContactUpdateView(UpdateView):
    model = Contacts
    fields = (
        "id",
        "name",
        "date_of_birth",
        "avatar",
    )
    template_name_suffix = "_update_form"


class ContactCreateView(CreateView):
    model = Contacts
    fields = (
        "name",
        "phone",
        "date_of_birth",
        "avatar",
    )

    def get_success_url(self):
        return reverse_lazy("contacts:create")


class ContactDeleteView(DeleteView):
    model = Contacts

    def get_success_url(self):
        return reverse_lazy("contacts:delete", kwargs={"pk": self.object.pk})


def show_all_to_edit(request: HttpRequest) -> HttpResponse:
    contacts = Contacts.objects.all()
    return render(
        request, "contacts/edit.html", {"title": "Contacts", "contacts": contacts}
    )


def show_all_to_delete(request: HttpRequest) -> HttpResponse:
    contacts = Contacts.objects.all()
    return render(
        request, "contacts/delete.html", {"title": "Contacts", "contacts": contacts}
    )


# def delete_contact(request: HttpRequest, pk) -> HttpResponse:
# contact = Contacts.objects.get(pk=pk)
# form = ContactsForm(instance=contact)
# contact.delete()
# return render(
# request,
# "contacts/contacts_confirm_delete.html",
# {"title": "Delete contact", "form": form, "contact": contact},
# )
