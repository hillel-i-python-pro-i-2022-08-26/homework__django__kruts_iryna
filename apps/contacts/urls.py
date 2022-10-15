from django.urls import path

from apps.contacts import views

app_name = "contacts"

urlpatterns = [
    path("", views.show_all_contacts, name="index"),
    path("<int:pk>", views.edit_contact, name="edit"),
    path("create_contact/", views.create_contact, name="create_contact"),
    path("delete_contact/<int:pk>/", views.delete_contact, name="delete"),

]
