import os
from pathlib import Path
from decouple import config

from django.contrib.messages import constants as messages
from django.utils.translation import gettext_lazy as _


#!Your everywhere service name
SITE_NAME = ""  # Domain Name

#!Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


#!App Name
APP_NAME = "BOOK"  # Default ADMIN,BOOK

#!SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")


#!# PROD, LOCAL, DEV
ENVIRONMENT = config("ENVIRONMENT", default="LOCAL")
ALLOWED_HOSTS = (
    []
)  # In order to allow access to the Django app from any server or IP address,ensure ALLOWED_HOSTS in settings.py file set to *,as shown in the left

if ENVIRONMENT != "LOCAL":
    pass
else:
    ALLOWED_HOSTS.append("*")


#!Application definition
DEFAULT_APPS = [
    "jet.dashboard",
    "jet",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

#!Third Part App
THIRD_PARTY_APPS = [
    "django_cleanup",
    "ckeditor",
    "django_extensions",
    "django_countries",
    "import_export",
    "tailwind",
    "django_browser_reload",
    "widget_tweaks",
    "djmoney",
    "django_celery_beat",  # This extension enables you to store the periodic task schedule in the database, Defined Name At Admin Panel => Periodic Tasks
    "django_celery_results",  # This extension enables you to store Celery task results using the Django ORM.This extension logging celery tasks and after saved all data in database
]

#!Created Apps
CREATED_APPS = [
    "theme",
    "abstract",
    "apps.author",
    "apps.book",
    "apps.customer",
    "apps.publisher",
    "apps.rental",
    "apps.cart",
    "apps.account",
]

#!Installed Apps
INSTALLED_APPS = DEFAULT_APPS + CREATED_APPS + THIRD_PARTY_APPS


#!AUTH_USER_MODEL
AUTH_USER_MODEL = "account.Account"


TAILWIND_APP_NAME = "theme"
INTERNAL_IPS = [
    "127.0.0.1",
]
NPM_BIN_PATH = config("NPM_BIN_PATH")

#!Middleware
MIDDLEWARE = [
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "apps.account.middleware.RedirectAuthenticatedMiddleware",
]

#!Root UrlConf
ROOT_URLCONF = "config.urls"

#!Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

#!Wsgi Application
WSGI_APPLICATION = "config.wsgi.application"


#!AUTH USER MODEL
# AUTH_USER_MODEL = 'account.Account'

#!Auth Password Validators
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

#!Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/
LANGUAGE_CODE = "en"  # production => az

LANGUAGES = [
    ("az", _("Azerbaijani")),
    ("en", _("English")),
    ("ru", _("Russian")),
]
TIME_ZONE = "Asia/Baku"
USE_I18N = True  # A boolean that specifies whether Django's translation system should be enabled
# USE_L10N = True #Numbers and dates using the format of the current locale.
USE_TZ = True  # A boolean indicating whether time zones are used in the application.


#!DATE_INPUT_FORMATS
# DATE_INPUT_FORMATS = ['%m-%d-%Y']


#!Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = "static/"


#!Default Auto Field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


#!Static Files
ENVIRONMENT = config("ENVIRONMENT")
if ENVIRONMENT == "LOCAL" or ENVIRONMENT == "PROD":
    # STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
    STATIC_ROOT = os.path.join(BASE_DIR, "static")
# else:#if site deployed to production
#     STATIC_ROOT = os.path.join(BASE_DIR,'static')#for production


#!MediuUrl and MediaRoot
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


#!Ckeditor Configuration
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_JQUERY_URL = "//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"
CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": "full",
        "width": "auto",
        "extraPlugins": ",".join(
            [
                "codesnippet",
            ]
        ),
    },
}


#!Jet Themes
JET_THEMES = [
    {
        "theme": "default",  # theme folder name
        "color": "#47bac1",  # color of the theme's button in user menu
        "title": "Default",  # theme title
    },
    {"theme": "violet", "color": "#a464c4", "title": "Violet"},
    {"theme": "green", "color": "#44b78b", "title": "Green"},
    {"theme": "light-green", "color": "#2faa60", "title": "Light Green"},
    {"theme": "light-violet", "color": "#a464c4", "title": "Light Violet"},
    {"theme": "light-blue", "color": "#5EADDE", "title": "Light Blue"},
    {"theme": "light-gray", "color": "#222", "title": "Light Gray"},
]


#!MESSAGE_TAGS
MESSAGE_TAGS = {
    messages.ERROR: "danger",
}


#!Celery

# Localhost
# CELERY_BROKER_URL = 'redis://localhost:6379'
# CELERY_RESULT_BACKEND = "redis://localhost:6379"

# Docker
CELERY_BROKER_URL = config(
    "CELERY_BROKER_URL", "amqp://guest:guest@rabbitmq:5672/"
)  # Second 'redis' keyword refer container name of redis
CELERY_RESULT_BACKEND = config("CELERY_RESULT_BACKEND", "redis://redis:6379")


#!Django Celery Results Configuration
CELERY_RESULT_BACKEND = "django-db"  # => django_celery_results

#!Django Celery Beat Configuration
CELERY_BEAT_SCHEDULER = (
    "django_celery_beat.schedulers.DatabaseScheduler"  # => django_celery_beat
)



