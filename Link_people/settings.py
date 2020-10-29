"""
Django settings for Link_people project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path

import environ

import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent




env = environ.Env(
    # set casting, defalut value
    DEBUG=(bool, False)
)

ENVIRONMENT = os.environ.get('ENVIRONMENT', default='development')


if ENVIRONMENT == 'production':
    env_file = os.path.join(BASE_DIR, ".env")

    # reading .env file
    environ.Env.read_env(env_file)

# False if not in os.environ
DEBUG = env('DEBUG', default=False)



# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ, So provided default value
SECRET_KEY = env("SECRET_KEY", default="unsafe-secret-key")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/



ALLOWED_HOSTS = ['linkpeople.herokuapp.com/', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Third-party
    'crispy_forms',
    'allauth',
    'allauth.account',
    'debug_toolbar',

    # Local
    'pages.apps.PagesConfig',
    'users.apps.UsersConfig',
    'user_profile.apps.UserProfileConfig',
    'jobs.apps.JobsConfig',
    'get_premium.apps.GetPremiumConfig',
    'orders.apps.OrdersConfig',
]


CRISPY_TEMPLATE_PACK = 'bootstrap4'



MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = 'Link_people.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'Link_people.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {

     # read os.environ['DATABASE_URL'] and raises ImproperlyConfigured exception if not found
    'default': env.db(),

}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'


# defines the location of static files in local development
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),] 

# location of static files for production 
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# It is implicitly set for us and although this is an optional step, I prefer to make it explicit in all projects.
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# use CustomUser instead of the default User model.
AUTH_USER_MODEL = 'users.CustomUser' 


LOGIN_REDIRECT_URL = 'home'
# LOGOUT_REDIRECT_URL = 'home' # for django auth
ACCOUNT_LOGOUT_REDIRECT_URL = 'home' # for allauth


SITE_ID = 1



AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_USERNAME_REQUIRED = False
#ACCOUNT_USER_MODEL_USERNAME_FIELD = None
#ACCOUNT_USER_MODEL_EMAIL_FIELD = None
ACCOUNT_AUTHENTICATION_METHOD = 'email'



ACCOUNT_FORMS = {'signup': 'users.forms.CustomUserCreationForm'}


DEFAULT_FROM_EMAIL = 'admin@linkpeople.com'





#SILENCED_SYSTEM_CHECKS = ["auth.W004"]



EMAIL_HOST = env('EMAIL_HOST')
EMAIL_USE_TLS = env('EMAIL_USE_TLS')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')


# Settings for Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



# Stripe
STRIPE_TEST_PUBLISHABLE_KEY=os.environ.get('STRIPE_TEST_PUBLISHABLE_KEY')
STRIPE_TEST_SECRET_KEY=os.environ.get('STRIPE_TEST_SECRET_KEY')


# Django-debug-toolbar
INTERNAL_IPS = ('127.0.0.1',)


# set three additional fields to add per-site caching
CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 604800 # number of seconds to cache a page. After the period is up, the cache expires and becomes empty.
CACHE_MIDDLEWARE_KEY_PREFIX = ''



# security settings
if ENVIRONMENT == 'production':
    SECURE_BROWSER_XSS_FILTER = True # To help guard against XSS attacks
    X_FRAME_OPTIONS = 'DENY'
    SECURE_SSL_REDIRECT = True

    # web browsers should only interact via HTTPS
    SECURE_HSTS_SECONDS = 3600
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True # otherwise your site may still be vulnerable via an insecure connection to a subdomain.
    SECURE_HSTS_PRELOAD = True
    SECURE_CONTENT_TYPE_NOSNIFF = True

    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True


    # dj-database-url
    db_from_env = dj_database_url.config(conn_max_age=500) # Returns configured DATABASE dictionary from DATABASE_URL
    DATABASES['default'].update(db_from_env)