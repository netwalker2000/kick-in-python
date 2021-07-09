"""
Django settings for productProject project.

Generated by 'django-admin startproject' using Django 1.11.29.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import pymysql

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c7l9*d6(6tct4ap2wyet$vo+e)4m-2sy4eykuefz6rp0myca39'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# Application definition
ADMIN_DISABLE = True
INSTALLED_APPS = [
    "productApp",
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE_CLASSES = [
    "productProject.exception.CustomizedException"
]

ROOT_URLCONF = 'productProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'productProject.wsgi.application'

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

pymysql.install_as_MySQLdb()

# Cache
CACHE_TIMEOUT = 1800
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'OPTIONS': {
            'MAX_ENTRIES': 1000,
        }
    }
}

# logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    # 'incremental': True,
    'root': {
        'level': 'DEBUG',
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
            # 'filename': 'entry_test_benchmark.log',
        },
    },
    'loggers': {
        'bench': {
            'handlers': ['file'],
            'level': 'DEBUG',
        }
    }
}

# db settings
DATABASES = {
    'default': {
        'NAME': 'product_db',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': 3306,
    },
    'comment_shard_1': {
        'NAME': 'comment_shard_1',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': 3306,
    },
    'comment_shard_2': {
        'NAME': 'comment_shard_2',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': 3306,
    },
}

# Connection with TCP servers
TCP_SERVERS = {
    'default': {
        'TCP_HOST': '10.143.143.25',
        'TCP_PORT': 8001,
        'TCP_NUM_CONNECTIONS': 50,
        'TCP_TIMEOUT_SECONDS': 60,
    },
}

SECRET_OF_TOKEN = "dsffT5%1regvvrg$$"

try:
    from dev_settings import *
except ImportError:
    pass