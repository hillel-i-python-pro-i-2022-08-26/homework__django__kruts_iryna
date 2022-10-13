from django.urls import path

from apps.contacts import views


urlpatterns = [
    path("", views.index, name="index"),
]