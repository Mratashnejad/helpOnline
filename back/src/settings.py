from pathlib import Path
from .secrets import DJANGO_SECRET_KEY, JWT_SECRET_KEY
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = DJANGO_SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

#site id for allauth # dont touch it !!!
SITE_ID = 1
#site id for allauth # dont touch it !!!

WSGI_APPLICATION = "src.wsgi.application"

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    
    #local apps
    "users",
    "consultation",
    

    #third party
    'rest_framework',
    "rest_framework.authtoken",
    "corsheaders",
    "django.contrib.sites",


    #authentication
    'dj_rest_auth',
    'dj_rest_auth.registration',

    #allauth
    'allauth',
    'allauth.account',
    'django.contrib.auth',
    'django.contrib.messages',

    
    #social accounts
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.yandex',

]

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    
    'google': {
       'SCOPE':[
           'profile',
           'email'
       ],
       'AUTH_PARAMS' : {'access_type' : 'online',}
        
    }
}

SOCIALACCOUNT_EMAIL_VERIFICATION = "none"
SOCIALACCOUNT_EMAIL_REQUIRED = "FALSE"
REST_USE_JWT = True



MIDDLEWARE = [
    
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    

    "corsheaders.middleware.CorsMiddleware", 
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

#JSON WEB TOKEN

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME'    : timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME'   : timedelta(days=7),
    'ROATATE_REFRESH_TOKEN'    : True,
    'BLACKLIST_AFTER_ROTATION' : True,
    'UPDATE_LAST_LOGIN'        : True,
    "USER_ID_FIELD"            : "userId", #for custom Model
    "USER_ID_CLAIM"            : "user_id",
    "SIGNING_KEY"              : JWT_SECRET_KEY
}

#must be change affter publishing
CORS_ORIGIN_ALLOW_ALL = True

#custom user model , because we dont want to use DJANGO provided user models
AUTH_USER_MODEL = "users.CustomUserModel"

#our exact serializer for django-rest-auth
REST_AUTH_SERIALZERS = {
    'USER_DETAILS_SERIALIZER' : 'users.serializers.CustomUserModelSerializer'
}

REST_FRAMEWORK ={
    "DEFAULT_PERMISSION_CLASSES" :(
        'rest_framework.permissions.IsAuthenticated',
   
    ),
    "DEFAULT_AUTHENTICATION_CLASSESS" : (
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "dj_rest_auth.utils.JWTCookieAuthentication",
    ),
}

ROOT_URLCONF = "src.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                 # `allauth` needs this from django
                "django.template.context_processors.request",

            ],
        },
    },
]





# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
