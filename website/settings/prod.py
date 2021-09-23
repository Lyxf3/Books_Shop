import os

from .django import *
from .project import *
from .third_party import *

SECRET_KEY = 'Z.7um>Da=kWXFeA7vr,grYg+)Sk/7u"-#suw`[?H'

DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'NAME': os.environ.get('DATABASE_NAME'),
        'PORT': os.environ.get('DATABASE_PORT'),
        'USER': os.environ.get('DATABASE_USER'),
        'ENGINE': os.environ.get('ENGINE')
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}

MIDDLEWARE = ['django.middleware.cache.UpdateCacheMiddleware'] + \
             MIDDLEWARE + \
             ['django.middleware.cache.FetchFromCacheMiddleware']

print(">>> START PROJECT WITH PROD SETTINGS <<<")