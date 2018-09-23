"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 1.11.12.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ihu@*w8*crlretq1gn@pw7slgc98wl)m#p&bl86fv_)rlkv((j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'formtools',
    'articles',
    'accounts',
    'rest_framework',
    'django_filters',
    'geoposition',
    'paypal.standard.ipn',
    'postman',
    'star_ratings',









]



GEOPOSITION_GOOGLE_MAPS_API_KEY = 'AIzaSyCYf4jJIvgiDupPQJ-KzV0QYAj2slIrpck'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',


]

ROOT_URLCONF = 'app.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
)


ADMIN_MEDIA_PREFIX = STATIC_URL + "admin/"

MEDIA_URL = '/media/'



MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025


GEOPOSITION_GOOGLE_MAPS_API_KEY = 'AIzaSyCYf4jJIvgiDupPQJ-KzV0QYAj2slIrpck'

GEOPOSITION_MAP_OPTIONS = {
    'minZoom': 15,
    'maxZoom': 18,
}

GEOPOSITION_MARKER_OPTIONS = {
    'cursor': 'move'
}

USE_THOUSAND_SEPARATOR = True


FORMAT_MODULE_PATH = {
    'articles.formats'

}

DECIMAL_SEPARATOR = True



PAYPAL_TEST = True

POSTMAN_AUTO_MODERATE_AS = True

AUTH_PROFILE_MODULE = 'accounts.UserProfile'

DEFAULT_PORT = "8000"


STAR_RATINGS_RERATE = False

STAR_RATINGS_ANONYMOUS = True

STAR_RATINGS_STAR_HEIGHT = 15
STAR_RATINGS_STAR_WIDTH = 15
