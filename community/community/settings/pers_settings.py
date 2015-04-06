from .base import *

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'community',
        'USER': 'postgres',
        'PASSWORD': 'FunnyM0nk3y',
        'HOST':''
    }
}
