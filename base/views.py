from django.http import HttpRequest, HttpResponse

from base.services.get_some_mes import random_mes


def index(request: HttpRequest):
    return HttpResponse(random_mes())
