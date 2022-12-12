import datetime
import logging
from http import server
from http.client import HTTPConnection

from django.contrib.sites import requests
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpRequest, HttpResponse
from django.middleware import http
from django.shortcuts import render
from django.test import RequestFactory
from django.views.generic import ListView

# from apps.session.models import UserDataRequest

KEY__COUNT_OF_VISITS = "count_of_visits"


def session_example_view(request: WSGIRequest | HttpRequest) -> HttpResponse:
    session = request.session
    count_of_visits = session.get(KEY__COUNT_OF_VISITS, 0)
    visits_time = session.get("visits_time", datetime.datetime.now())
    count_of_visits += 1
    session[KEY__COUNT_OF_VISITS] = count_of_visits

# newcode


    #req = request.get('http://127.0.0.1:8000/')
    # user_name = request.user
    # req = request.get_host()
    # req1 = RequestFactory()


    return render(
        request,
        "session/index.html",
        {
            "session_id": session.session_key,
            "count_of_visits": count_of_visits,
            "visits_time": visits_time,
            "title": "Session example",
            # 'user_name': user_name,
            # 'req': req,
            # 'req1': req1
        },
    )

# class ArticleListView(ListView):
#     model = UserDataRequest
#     template_name = 'session/new.html'
#
# log = logging.getLogger('urllib3')  # works
#
# log.setLevel(logging.DEBUG)  # needed
# fh = logging.FileHandler("requests.log")
# log.addHandler(fh)
#
# requests.get('http://127.0.0.1:8000')
