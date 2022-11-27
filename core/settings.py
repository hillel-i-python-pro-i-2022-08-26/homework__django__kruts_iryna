"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import mimetypes
from pathlib import Path

# noinspection PyPackageRequirements
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
APPS_DIR = BASE_DIR.joinpath("apps")

env = environ.Env()
env.read_env(BASE_DIR.joinpath(".env"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("DJANGO__SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DJANGO__DEBUG", False)

ALLOWED_HOSTS = env.list("DJANGO__ALLOWED_HOSTS", default=[])

if DEBUG:
    import mimetypes
    mimetypes.add_type("application/javascript", ".js", True)


if DEBUG:
    ALLOWED_HOSTS.extend(
        [
            "0.0.0.0",
            "127.0.0.1",
            "localhost",
            "127.0.0.1:8000",
        ]
    )




    # mimetypes.add_type("application/javascript", ".js", True)

# if DEBUG:
#     import socket  # only if you haven't already imported this
#     hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
#     INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]
# Application definition

# import mimetypes
#
# mimetypes.add_type("application/javascript", ".js", True)

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "debug_toolbar",
]
LOCAL_APPS = [
    "apps.base",
    "apps.contacts",
    "apps.users",
    "apps.session",
]
THIRD_PARTY_APPS = [
    "crispy_forms",
    "crispy_bootstrap5",
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'debug_toolbar.middleware.DebugToolbarMiddleware',

]

ROOT_URLCONF = "core.urls"

AUTH_USER_MODEL = "users.User"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "apps/templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": env.db_url_config(
        # f'sqlite:///{BASE_DIR.joinpath("db", "db.sqlite3")}'
        # postgres://user:password@host:port/dbname
        env.str(
            "DJANGO__DB_URL",
            f'postgres://{env.str("POSTGRES_USER")}:{env.str("POSTGRES_PASSWORD")}'
            f'@{env.str("POSTGRES_HOST")}:{env.str("POSTGRES_PORT")}/{env.str("POSTGRES_DB")}',
        )
    )
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [
    APPS_DIR.joinpath("static"),
]
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field


MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR.joinpath("media")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_REDIRECT_URL = "/"

INTERNAL_IPS = [
    "127.0.0.1",
    "127.0.0.1:8000",

]



# DEBUG_TOOLBAR_CONFIG = {
#     'SHOW_TOOLBAR_CALLBACK': lambda _request: DEBUG
# }

# DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False,}

# DEBUG_TOOLBAR_CONFIG = {
#     'DISABLE_PANELS': [
#         'debug_toolbar.panels.redirects.RedirectsPanel',
#     ],
#     'SHOW_TEMPLATE_CONTEXT': True,
# }


# DEBUG_TOOLBAR_CONFIG = {
#     'SHOW_TOOLBAR_CALLBACK': lambda x: True
# }
#
# DEBUG_TOOLBAR_PATCH_SETTINGS = False
# debug_toolbar moved here.
# if DEBUG:
#     MIDDLEWARE += [
#         'debug_toolbar.middleware.DebugToolbarMiddleware',
#     ]
#     INSTALLED_APPS += [
#         'debug_toolbar',
#     ]
#     INTERNAL_IPS = ['127.0.0.1', ]
#
#     # this is the main reason for not showing up the toolbar
#     import mimetypes
#
#     mimetypes.add_type("application/javascript", ".js", True)
#
#     DEBUG_TOOLBAR_CONFIG = {
#         'INTERCEPT_REDIRECTS': False,
#     }
