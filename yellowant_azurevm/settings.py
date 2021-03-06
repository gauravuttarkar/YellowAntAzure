import os
import json


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DJANGO_ENV = os.environ.get("DJANGO_ENV", "heroku")

# get app credentials from json
CREDENTIALS = open(BASE_DIR + '../yellowant_app_credentials.json').read()
CREDENTIALS = json.loads(CREDENTIALS)

### YellowAnt specific settings ###
# URL to obtain oauth2 access for a YA user
if DJANGO_ENV == "development":
    YA_OAUTH_URL = "http://www.spendse.com/api/oauth2/authorize/"
    os.environ["YELLOWANT_API_URL"] = "http://api.spendse.com/api/%s"
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1"
else:
    YA_OAUTH_URL = "https://www.yellowant.com/api/oauth2/authorize/"

if DJANGO_ENV == "heroku":
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
    BASE_URL = "https://{}.herokuapp.com".format(HEROKU_APP_NAME)
else:
    BASE_URL = os.environ.get("BASE_URL", "https://83b6d5dd.ngrok.io")

# app_name = os.environ.get("HEROKU_APP_NAME")
# BASE_URL = "https://{}.herokuapp.com".format(app_name)
ALLOWED_HOSTS = ['*']
# BASE_URL = "https://83b6d5dd.ngrok.io"
BASE_HREF = "/"
SITE_PROTOCOL = "https://"

# BASE_URL = "https://d0e6f62c.ngrok.io"
# URL to receive oauth2 codes from YA for user authentication. As a developer, you need to provide this URL in the YA
# developer console so that YA knows exactly where to send the oauth2 codes.
YA_REDIRECT_URL = "{}/yellowant-oauth-redirect/".format(BASE_URL)

# Numerical ID generated when you register your application through the YA developer console
# YA_APP_ID = CREDENTIALS.get("application_id", None)
# # Client ID generated from the YA developer console. Required to identify requests from this application to YA
# YA_CLIENT_ID = CREDENTIALS.get('client_id')
# # Client secret generated from the YA developer console. Required to identify requests from this application to YA
# YA_CLIENT_SECRET = CREDENTIALS.get('client_secret')
# # Verification token generated from the YA developer console. This application can verify requests from YA as they will
# # carry the verification token
# YA_VERIFICATION_TOKEN = CREDENTIALS.get('verification_token')


YA_APP_ID = str(CREDENTIALS['application_id'])
YA_CLIENT_ID = str(CREDENTIALS['client_id'])
YA_CLIENT_SECRET = str(CREDENTIALS['client_secret'])
YA_VERIFICATION_TOKEN = str(CREDENTIALS['verification_token'])
### END YellowAnt specific settings ###


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#x9q+c*t9$=buk$i@m&6e+k@m(q@uds0gd=9=3cej6u#_u=m*%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: remove wildcard condition from ALLOWED_HOSTS
ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'yellowant_api',

    'web',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'yellowant_azurevm.urls'

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
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'yellowant_azurevm.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

if DJANGO_ENV == "heroku":
    import dj_database_url

    DATABASES = {
        'default': dj_database_url.config(
            default='sqlite:////{0}'.format(
                os.path.join(BASE_DIR, 'db.sqlite3'))
        )
    }
else:
    DATABASES = {
        # 'default': {
        #     'ENGINE': 'django.db.backends.sqlite3',
        #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # }
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'azure',
            'USER': "root",
            'PASSWORD': "root1234",
            'HOST': "localhost",
            'PORT': '',
        }
    }



# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'