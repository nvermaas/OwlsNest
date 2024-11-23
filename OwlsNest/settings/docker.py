from OwlsNest.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = ["https://uilennest.net"]
CORS_ORIGIN_ALLOW_ALL = True

FORCE_SCRIPT_NAME = os.environ.get('FORCE_SCRIPT_NAME', '/')

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '/shared/hiking.sqlite3'),
    }
}

