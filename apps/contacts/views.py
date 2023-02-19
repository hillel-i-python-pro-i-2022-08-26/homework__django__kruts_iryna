from django.forms import model_to_dict
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Contacts
from .forms import ContactsForm, UserForm
from rest_framework import generics

from ..serializers import ContactsSerializer


# class ContactAPIView(generics.ListAPIView):
#     queryset = Contacts.objects.all()
#     serializer_class = ContactsSerializer


class ContactAPIView(APIView):
    def get(self, requests):
        lst = Contacts.objects.all()

        return Response({'contacts': ContactsSerializer(lst, many=True).data})
    def post(self, request):
        serializer = ContactsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'contact': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Contacts.objects.get(pk=pk)
        except:
            return Response({"error": "Method PUT not allowed"})

        serializer = ContactsSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'contact': serializer.data})



def show_all_contacts(request: HttpRequest) -> HttpResponse:
    contacts = Contacts.objects.all()
    return render(
        request, "contacts/index.html", {"title": "Contacts", "contacts": contacts}
    )


def show_all_to_edit(request: HttpRequest) -> HttpResponse:
    contacts = Contacts.objects.all()
    return render(
        request, "contacts/edit.html", {"title": "Contacts", "contacts": contacts}
    )


def edit_contact(request: HttpRequest, pk: int) -> HttpResponse:
    contact = Contacts.objects.get(pk=pk)
    form = ContactsForm(instance=contact)
    return render(
        request, "contacts/edit_form.html", {"title": "Edit contact", "form": form}
    )


# https://www.youtube.com/watch?v=EX6Tt-ZW0so
def create_contact(request: HttpRequest) -> HttpResponse:
    form = UserForm()
    if request.method == "POST":
        # print("Printing POST:", request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {"form": form}
    return render(request, "contacts/create.html", context)


def show_all_to_delete(request: HttpRequest) -> HttpResponse:
    contacts = Contacts.objects.all()
    return render(
        request, "contacts/delete.html", {"title": "Contacts", "contacts": contacts}
    )


def delete_contact(request: HttpRequest, pk) -> HttpResponse:
    contact = Contacts.objects.get(pk=pk)
    form = ContactsForm(instance=contact)
    contact.delete()
    # context = {'contact': contact}
    return render(
        request,
        "contact/delete_form.html",
        {"title": "Delete contact", "form": form, "contact": contact},
    )
