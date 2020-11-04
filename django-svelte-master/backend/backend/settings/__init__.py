"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import datetime
import os

import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BACKEND_BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
APP_ROOT = os.path.dirname(BACKEND_BASE_DIR)
FRONTEND_BASE_DIR = f'{APP_ROOT}/frontend/web'

PYTHONPATH = "/Users/xiaofengcao/projects/d3_learning/django-svelte-master"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!``
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.herokuapp.com', '127.0.0.1']

CORS_ALLOW_CREDENTIALS = True

# TODO: add these
CORS_ORIGIN_WHITELIST = []
CSRF_TRUSTED_ORIGINS = ['volvita.herokuapp.com']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'backend.authentication_middleware_jwt.AuthenticationMiddlewareJWT',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(FRONTEND_BASE_DIR, 'public')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ]
        },
    }
]

WSGI_APPLICATION = 'backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases



# database

PG_USER = os.environ.get("PG_USER", "metaplay")
PG_PASSWORD = os.environ.get("PG_PASSWORD")
PG_HOST = os.environ.get("PG_HOST", "postgres-postgresql.postgres")
PG_PORT = os.environ.get("PG_PORT", "5432")
PG_DATABASE = os.environ.get("PG_DATABASE", "metaplay") # should update at some point soon
PG_CONN = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DATABASE}"
# DATABASES = {'default': dj_database_url.config()}
DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': PG_DATABASE,

        'USER': PG_USER,

        'PASSWORD': PG_PASSWORD,

        'HOST': PG_HOST,

        'PORT': PG_PORT,

    }

}
# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'
    },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SECURE_SSL_REDIRECT = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(FRONTEND_BASE_DIR, 'build/static')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

WHITENOISE_ROOT = os.path.join(FRONTEND_BASE_DIR, 'public')

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

JWT_AUTH = {
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'backend.utils.jwt_response_handler',
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=365),
}
