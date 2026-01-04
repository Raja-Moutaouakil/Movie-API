import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "django-insecure-local-dev-key")

# Read DEBUG from env. Accept several truthy values.
_dj_env = os.environ.get("DJANGO_DEBUG", "True")
DEBUG = str(_dj_env).lower() in ("1", "true", "yes")

# Read ALLOWED_HOSTS from env (comma-separated). If not provided and DEBUG is False,
# default to localhost addresses so local runs don't raise CommandError.
_allowed = os.environ.get("ALLOWED_HOSTS")
if _allowed:
	ALLOWED_HOSTS = [h.strip() for h in _allowed.split(",") if h.strip()]
else:
	ALLOWED_HOSTS = ["127.0.0.1", "localhost"] if not DEBUG else []

# Application definition
INSTALLED_APPS = [
	"django.contrib.admin",
	"django.contrib.auth",
	"django.contrib.contenttypes",
	"django.contrib.sessions",
	"django.contrib.messages",
	"django.contrib.staticfiles",
	"rest_framework",
	"django_filters",
	"drf_spectacular",
	"drf_spectacular_sidecar",
	"reviews",
]

MIDDLEWARE = [
	"django.middleware.security.SecurityMiddleware",
	"django.contrib.sessions.middleware.SessionMiddleware",
	"django.middleware.common.CommonMiddleware",
	"django.middleware.csrf.CsrfViewMiddleware",
	"django.contrib.auth.middleware.AuthenticationMiddleware",
	"django.contrib.messages.middleware.MessageMiddleware",
	"django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "movie_review_api.urls"

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
			],
		},
	},
]

WSGI_APPLICATION = "movie_review_api.wsgi.application"

# Database
DATABASES = {
	"default": {
		"ENGINE": "django.db.backends.sqlite3",
		"NAME": BASE_DIR / "db.sqlite3",
	}
}

# Password validation
AUTH_PASSWORD_VALIDATORS = []

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "/static/"

# Minimal DRF defaults (project previously used DRF)
REST_FRAMEWORK = {
	"DEFAULT_AUTHENTICATION_CLASSES": (
		"rest_framework_simplejwt.authentication.JWTAuthentication",
	),
	"DEFAULT_PERMISSION_CLASSES": (
		"rest_framework.permissions.IsAuthenticatedOrReadOnly",
	),
	"DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
	"DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
	"PAGE_SIZE": 10,
	"DEFAULT_FILTER_BACKENDS": (
		"django_filters.rest_framework.DjangoFilterBackend",
		"rest_framework.filters.SearchFilter",
	),
}

# End of file

# drf-spectacular OpenAPI settings
SPECTACULAR_SETTINGS = {
	"TITLE": "Movie Review API",
	"DESCRIPTION": "A simple API for movies and reviews (DRF + drf-spectacular).",
	"VERSION": "1.0.0",
}

