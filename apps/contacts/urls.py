from django.urls import path

from apps.contacts import views


urlpatterns = [
    path("", views.show_all_contacts, name="index"),
]