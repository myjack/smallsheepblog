"""
Django settings for smallsheepblog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASE_DIR = os.path.join(BASE_DIR,'blogdb').replace('\\','/')

#STATIC_URL = os.path.join(BASE_DIR,'static').replace('\\','/')
STATIC_URL = '/static/'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z@19_dgps@kx953^@+qb-sail(hax4-_a4i$@d-nj85a+-3yv%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'engine',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'smallsheepblog.urls'

WSGI_APPLICATION = 'smallsheepblog.wsgi.application'

STATIC_ROOT = os.path.join(BASE_DIR,'static').replace('\\','/')

# Additional locations of static files

STATICFILES_DIRS = (
    ("images", os.path.join(STATIC_ROOT,'images').replace('\\','/')),
    ("css", os.path.join(STATIC_ROOT,'css').replace('\\','/')),
    ("js", os.path.join(STATIC_ROOT,'js').replace('\\','/')),
	#("custom-plugins", os.path.join(STATIC_ROOT,'custom-plugins').replace('\\','/')),
	#("jui", os.path.join(STATIC_ROOT,'jui').replace('\\','/')),
	#("plugins", os.path.join(STATIC_ROOT,'plugins').replace('\\','/')),
	#("bootstrap", os.path.join(STATIC_ROOT,'bootstrap').replace('\\','/')),
	#("swf", os.path.join(STATIC_ROOT,'swf').replace('\\','/')),
	# Put strings here, like "/home/html/static" or "C:/www/django/static".
	# Always use forward slashes, even on Windows.
	# Don't forget to use absolute paths, not relative paths.
)

TEMPLATE_DIRS = (
    'templates',
	# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
	# Always use forward slashes, even on Windows.
	# Don't forget to use absolute paths, not relative paths.
)


# Database

# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DATABASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

