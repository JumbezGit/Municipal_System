import os

import dj_database_url

from .settings import *
from .settings import BASE_DIR


def _split_env_list(name):
    value = os.environ.get(name, "")
    return [item.strip() for item in value.split(",") if item.strip()]


DEBUG = os.environ.get("DEBUG", "False").lower() == "true"
SECRET_KEY = os.environ.get("SECRET_KEY", SECRET_KEY)

allowed_hosts = _split_env_list("ALLOWED_HOSTS")
render_host = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
if render_host and render_host not in allowed_hosts:
    allowed_hosts.append(render_host)
ALLOWED_HOSTS = allowed_hosts

DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("DATABASE_URL"),
        conn_max_age=600,
        conn_health_checks=True,
    )
}

frontend_origins = _split_env_list("FRONTEND_URL")
if frontend_origins:
    CORS_ALLOWED_ORIGINS = frontend_origins

CSRF_TRUSTED_ORIGINS = frontend_origins

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

STATIC_ROOT = BASE_DIR / "staticfiles"
<<<<<<< HEAD
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG
=======

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

allowed_hosts_env = os.environ.get('ALLOWED_HOSTS', '')
ALLOWED_HOSTS = [host.strip() for host in allowed_hosts_env.split(',') if host.strip()]

# Render sets this at runtime, so include it automatically.
render_host = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if render_host and render_host not in ALLOWED_HOSTS:
    ALLOWED_HOSTS.append(render_host)
>>>>>>> 2c7bb8d61a94ce6909fdbb21825a01469070aa5f

