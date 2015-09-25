import os
DJANGO_DIR = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
BASE_DIR = os.path.abspath(os.path.dirname(DJANGO_DIR))


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'ecampaign',  # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'ecampaign',
        'PASSWORD': 'ecampaign',
        'HOST': 'localhost',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '5432',  # Set to empty string for default.
    }
}


WSGI_APPLICATION = 'ecampaign.wsgi.application'

########## MANAGER CONFIGURATION
#developers are requested to copy below settings in their own settings and modified as required.
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (('Rohan', 'rohan.nagalkar@vertisinfotech.com'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = (('Rohan', 'rohan.nagalkar@vertisinfotech.com'))
########## END MANAGER CONFIGURATION

ALLOWED_HOSTS = ['*']

# EMAIL Server config
EMAIL_HOST = 'smtp.vertis'
EMAIL_PORT = '25'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'noreply@vertisinfotech.com'


DEBUG_TOOLBAR_PATCH_SETTINGS = False #this needs to be kept false when running with wsgi


DEBUG=True
EMAIL_SUBJECT_PREFIX = 'Ecampaign.Vertis'

STATIC_URL = '/static/'
STATIC_ROOT = '/home/rohan/workspace/Ecampaign/static'

MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/rohan/workspace/Ecampaign/media'


TIME_ZONE = 'Asia/Calcutta'
