from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse('hello')