"""
Django settings for yga_data_warehouse project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
from os.path import dirname


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = dirname(dirname(dirname(os.path.abspath(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z576+$35yhxo3gu4opw()n^0*9ilb7=ue+7r_5@9_ltl9#35^3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'conformed_dimensions.apps.ConformedDimensionsConfig',
    'zip_codes.apps.ZipCodesConfig',
    'elastic.apps.ElasticConfig',
    'djcelery',
    'djkombu',
    'kombu.transport.django',
    'djsupervisor',
    'taggit',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'yga_data_warehouse.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'yga_data_warehouse.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'db.sqlite3'),
    },

    'oasis_db': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'WinOASIS',
        'USER': 'lathropk',
        'PASSWORD': 'wX8pG6ntcHDx',
        'HOST': 'ygasql02',
        'READONLY': True
    },
    'micros_db': {
        'NAME': 'PMDW',
        'ENGINE': 'sql_server.pyodbc',
        'HOST': 'ygasql03',
        'USER': 'PMDW',
        'PASSWORD': 'micros01',
        'OPTIONS': {
            'host_is_server': True,        
        },
    },
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}




# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'MST'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/warehouse/static/'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    )
}


# Celery settings  
# also update the db with: python manage.py migrate kombu_transport_django
import djcelery
djcelery.setup_loader()
CELERY_IMPORTS = ("conformed_dimensions.tasks", "elastic.tasks", )
CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend'
BROKER_URL = 'django://' 
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
#: Only add pickle to this list if your broker is secured 
#: from unwanted access (see userguide/security.html) 
CELERY_ACCEPT_CONTENT = ['json'] 
CELERY_TASK_SERIALIZER = 'json' 
CELERY_RESULT_SERIALIZER = 'json' 

# sqlalchemy connection to oasis database
from sqlalchemy import create_engine
OASIS_ENGINE = create_engine('mssql+pyodbc://lathropk:wX8pG6ntcHDx@ygasql02/WinOasis?driver=SQL+Server')

#elasticsearch connection
ES_HOST = "https://admin:santafe1@33c192f38ba000038f45d61b4fe43cac.us-east-1.aws.found.io:9243/"

CASINO_GEO_POINT = (34.5400242, -112.4685025)