"""
Django settings for evalai project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import datetime
import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPS_DIR = os.path.join(BASE_DIR, "apps")

sys.path.append(APPS_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "random_secret_key")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEST = False

ALLOWED_HOSTS = []


# Application definition

DEFAULT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
]

OUR_APPS = [
    "accounts",
    "analytics",
    "base",
    "challenges",
    "hosts",
    "jobs",
    "participants",
    "web",
]

THIRD_PARTY_APPS = [
    "allauth",
    "allauth.account",
    "corsheaders",
    "django_ses",
    "import_export",
    "rest_auth",
    "rest_auth.registration",
    "rest_framework.authtoken",
    "rest_framework",
    "rest_framework_docs",
    "rest_framework_expiring_authtoken",
    "drf_yasg",
]

INSTALLED_APPS = DEFAULT_APPS + OUR_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "evalai.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "evalai.wsgi.application"


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"  # noqa
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

SITE_ID = 1

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": (
        "rest_framework.pagination.LimitOffsetPagination"
    ),
    "PAGE_SIZE": 100,
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly"
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_expiring_authtoken.authentication.ExpiringTokenAuthentication"
    ],
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    "DEFAULT_THROTTLE_CLASSES": (
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ),
    "DEFAULT_THROTTLE_RATES": {"anon": "100/minute", "user": "100/minute"},
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
}

# ALLAUTH SETTINGS
ACCOUNT_EMAIL_REQUIRED = True
OLD_PASSWORD_FIELD_ENABLED = True
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = (
    "/api/auth/email-confirmed/"
)
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = (
    "/api/auth/email-confirmed/"
)

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

# CORS Settings
CORS_ORIGIN_ALLOW_ALL = True

# REST Framework Expiring Tokens Configuration
EXPIRING_TOKEN_LIFESPAN = datetime.timedelta(days=365)

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "root": {"level": "INFO", "handlers": ["console"]},
    "filters": {
        "require_debug_false": {"()": "django.utils.log.RequireDebugFalse"},
        "require_debug_true": {"()": "django.utils.log.RequireDebugTrue"},
    },
    "formatters": {
        "simple": {
            "format": "[%(asctime)s] %(levelname)s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "verbose": {
            "format": "[%(asctime)s] %(levelname)s %(module)s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "logfile": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(BASE_DIR, "django.log"),
            "maxBytes": 50000,
            "backupCount": 10,
            "formatter": "verbose",
        },
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
            "filters": ["require_debug_false"],
        },
    },
    "loggers": {
        "django": {"handlers": ["console"], "propagate": False},
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": False,
        },
        "django.security": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": False,
        },
        "django.db.backends": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": False,
        },
    },
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache"
    }
}

# The maximum size in bytes for request body
# https://docs.djangoproject.com/en/1.10/ref/settings/#data-upload-max-memory-size
FILE_UPLOAD_MAX_MEMORY_SIZE = 524288000  # 500 MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 524288000  # 500 MB

# To make usermame field read-only, customized serializer is defined.
REST_AUTH_SERIALIZERS = {
    "USER_DETAILS_SERIALIZER": "accounts.serializers.ProfileSerializer"
}

# For inviting users to participant and host teams.
ADMIN_EMAIL = "admin@cloudcv.org"
CLOUDCV_TEAM_EMAIL = "EvalAI Team <team@cloudcv.org>"
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'youremail@gmail.com'
EMAIL_HOST_PASSWORD = 'yourpassword'
EMAIL_PORT = 587

SWAGGER_SETTINGS = {
    "DEFAULT_INFO": "evalai.urls.swagger_api_info",
    "SECURITY_DEFINITIONS": {
        "Token Authentication": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
        }
    },
}

REDOC_SETTINGS = {"SPEC_URL": ("docs.yaml", {"format": ".yaml"})}

HOSTNAME = os.environ.get("HOSTNAME")

SENDGRID_SETTINGS = {
    "TEMPLATES": {"CHALLENGE_INVITATION": "d-60825bcf014f4958bdb1b9173471d420"}
}
