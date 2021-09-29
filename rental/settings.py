"""
Django settings for rental project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import  os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lt5f!q=x@k9g3s^o001c)g=1k+rb60i^7r5rd0!60mu-in7h($'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'user',
    'main',
    'features',
    'imguploading',
    'frontend_w_r',
    'froentendR',
    # 3d party
    'widget_tweaks',
    'rest_framework',
    'martor',



]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'rental.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates'),BASE_DIR/"froentendR/"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'social_django.context_processors.backends', # add this
                # 'social_django.context_processors.login_redirect', # add this
            ],
        },
    },
]

WSGI_APPLICATION = 'rental.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTHENTICATION_BACKENDS = [
    # 'social_core.backends.linkedin.LinkedinOAuth2',
    # 'social_core.backends.instagram.InstagramOAuth2',
    # 'social_core.backends.facebook.FacebookOAuth2',
    'user.backends.EmailBackend',
    # 'django.contrib.auth.backends.ModelBackend',
    ]

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

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
LOGIN_REDIRECT_URL = "user:profile"
LOGIN_URL='user:login'
LOGOUT_URL = 'user:logout'
LOGOUT_REDIRECT_URL = 'user:login'

STATIC_URL = '/static/'
MEDIA_URL ='/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
STATICFILES_DIRS = [
    BASE_DIR/"frontend_w_r/build/static/",
    BASE_DIR/"froentendR/build/static/",
    os.path.join(BASE_DIR, './static/static_dir'),
]
STATIC_ROOT = os.path.join(BASE_DIR,'./static/static_root/')

EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER='abdur963rahman@gmail.com'
EMAIL_HOST_PASSWORD='nzpfrtpajldijohh'

from .rest_setting import  *
from .cors_header import  *

# socal login
# first install this app
# pip install  social-auth-app-django
INSTALLED_APPS+=['social_django']
# fb loign
SOCIAL_AUTH_FACEBOOK_KEY = '672452203475296'        # App ID
SOCIAL_AUTH_FACEBOOK_SECRET =  '5ea038e5e0b4737bf47357e396d042bb' # App Secret
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']#, 'user_link'] # add this
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {       # add this
  'fields': 'id, name, email, picture.type(large) '#link'
}
#  the value is a list of attributes that should be returned by Facebook when the user has successfully logged in.
# The values are dependent on SOCIAL_AUTH_FACEBOOK_SCOP .

SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [                 # add this
    ('name', 'name'),
    ('email', 'email'),
    ('picture', 'picture'),
    # ('link', 'profile_url'),
]
# API returns the data requested in SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS. To store the data in the database, we need to specify them in SOCIAL_AUTH_FACEBOOK_EXTRA_DATA.


from .martor_config import *