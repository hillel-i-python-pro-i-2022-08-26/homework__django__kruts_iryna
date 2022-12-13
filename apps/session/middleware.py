from django.http import request, HttpRequest, response, HttpResponse
from django.middleware.csrf import logger
from django.contrib.auth import get_user

from django.contrib.auth.middleware import RemoteUserMiddleware

from apps.session.models import UserDataRequest


class CountRequestsMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        self.count_requests = 0
        self.count_exceptions = 0

    def __call__(self, request, *args, **kwargs):
        # session_key = request.session
        host = request.META["HTTP_HOST"] # получаем адрес сервера
        path = request.path  # получаем запрошенный путь
        user = request.user # user info
        # session = request.session #session key

        self.count_requests += 1

        # self.path = request.path
        logger.info(f"Handled {self.count_requests} requests. User : {get_user(request)}")
        print(get_user(request))
        if not request.session.session_key:
            request.session.save()
        session_key = request.session.session_key
        visitor = UserDataRequest.objects.filter(
            path_to_request=path, session_key=session_key, user=get_user(request)
        ).first()
        if visitor is None:
            visitor = UserDataRequest.objects(get_user(request), request.path, session_key)
            # visitor = UserDataRequest.objects(get_user(request), request.path, session_key)

        visitor = visitor.count() + 1
        visitor.save()

        return self.get_response(request)
        # return response



    def process_exception(self, request, exception):
        self.count_exceptions += 1
        logger.error(f"Encountered {self.count_exceptions} exceptions so far")

# import time
#
# from django.http import request
#
# from apps.contacts.models import Contacts
#
#
# class MessMiddleWare(object):
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         mycustom = Contacts.objects.filter(id=request.user.pk)
#         # Instead of using filter, consider doing (if it fits your usecase):
#         # mycustom = get_object_or_404(MyCustom, pk=request.user.pk)
#         request.mycustom = mycustom
#         response = self.get_response(request)
#         return response
#
#     def timing(get_response):
#         t1 = time.monotonic()
#         response = get_response(request)
#         t2 = time.monotonic()
#         print("TOTAL TIME:", (t2 - t1))
#         print('dsdddddd')
#         return response
# from django.http import HttpResponse
#
#
# class TestMiddleware:
#     def __int__(self, get_response: callable):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         print('afte')
#         #Before response
#         response = self.get_response(request)
#         print('before')
#         return response
#
# import time
#
#
#
#
# # import logging
# # from .models import UserDataRequest
# #
# # from django.http import HttpResponse
# #
# # # Get an instance of a logger
# # logger = logging.getLogger(__name__)
# #
# #
# # class CustomMiddleware:
# #     def __init__(self, get_response):
# #         self.get_response = get_response
# #         self.logger = logging.getLogger('django')
# #
# #     def __call__(self, request):
# #         session = request.session
# #         req = request.path
# #
# #         logger_message = f'{request.path}'
# #         self.logger.info(f"Before ------------- {logger_message}, {session}")
# #
# #
# #         response = self.get_response(request)
# #
# #         self.logger.info(f"After ---------------- {logger_message}")
# #
# #
# #         #end_time = time.monotonic()
# #
# #
# #         return response
# #
# #     def add_info_to_db(self):
# #         UserDataRequest.objects.create(path_to_request=req)
#
#
#
#
# import socket
# import time
# import json
# import logging
#
# from django.contrib.auth import SESSION_KEY, BACKEND_SESSION_KEY, load_backend
#
# from apps.session.models import UserDataRequest
#
# request_logger = logging.getLogger(__name__)
# def get_user(request):
#     from django.contrib.auth.models import AnonymousUser
#     try:
#         user_id = request.session[SESSION_KEY]
#         backend_path = request.session[BACKEND_SESSION_KEY]
#         backend = load_backend(backend_path)
#         user = backend.get_user(user_id) or AnonymousUser()
#     except KeyError:
#         user = AnonymousUser()
#     return user
#
#
#
# class RequestLogMiddleware:
#     """Request Logging Middleware."""
#
#     def __init__(self, get_response):
#         self.get_response = get_response
#         self.logger = logging.getLogger('django')
#
#     def __call__(self, request):
#
#         log_data = {
#             # "user_name": request.user.first_name,
#             # "user_name": get_user(request),
#             "user_name": request.user,
#             "session_id" : request.session,
#             "server_hostname": socket.gethostname(),
#             "request_method": request.method,
#             "request_path": request.get_full_path(),
#         }
#
#
#         # UserDataRequest.objects.create(
#         #     path_to_request=log_data["user_name"],
#         #     session_key=log_data["session_id"],
#         #     # user=str(log_data["request_path"])
#         # )
#
#         response = self.get_response(request)
#
#         # self.logger.info(f"Before ------------- {log_data}")
#
#
#
#         return response
#
#     # Log unhandled exceptions as well
#     def process_exception(self, request, exception):
#         try:
#             raise exception
#         except Exception as e:
#             request_logger.exception("Unhandled Exception: " + str(e))
#         return exception



