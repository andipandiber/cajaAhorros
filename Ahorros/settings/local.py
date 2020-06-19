
from .base import *

DEBUG = True

ALLOWED_HOSTS = []

# Database
DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME':  get_secret('DB_NAME'),
            'USER':  get_secret('USER'),
            'PASSWORD': get_secret('PASSWORD'),
            'HOST': 'localhost',
            'PORT': '3306',
            'TEST' : {
                'NAME' : 'test_bd',
            },
    }
}

# Static files (CSS, JavaScript, Images)


STATIC_URL = '/static/'
STATICFILE_DIRS = [BASE_DIR.child('static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')