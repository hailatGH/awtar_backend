import os
import django
from pathlib import Path
from urllib.parse import urlparse
from django.utils.encoding import force_str
    
django.utils.encoding.force_text = force_str

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-5vxjrkj0@3kok#r(0-$l3co7q1omml%444!18&37xocwp-v#6-')

DEBUG = True
if os.environ.get('DEBUG') == "True":
    DEBUG = True

LOCAL = False
if os.environ.get('LOCAL') == "True":
    LOCAL = True

URL = os.environ.get('URL')
# URL = 'https://awtar-backend-api.calmgrass-743c6f7f.francecentral.azurecontainerapps.io'
if URL:
    if LOCAL:
        ALLOWED_HOSTS = list(URL.split(','))
    else:
        ALLOWED_HOSTS = [urlparse(URL).netloc]
        CSRF_TRUSTED_ORIGINS = [URL]
        CORS_ORIGIN_ALLOW_ALL = True
        CORS_ALLOW_CREDENTIALS = True
        # CORS_ORIGIN_WHITELIST = ['http://localhost:5173']
        # CORS_ALLOW_ALL_ORIGINS = True

else:
    ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Installed Apps
    'corsheaders',
    'drf_yasg',
    'rest_framework',
    'storages',
    'django_filters',
    'django.contrib.postgres.search',
    
    # Custom Apps
    'music',
    'search_app',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': os.environ.get('POSTGRES_DB'),
#         'USER': os.environ.get('POSTGRES_USER'),
#         'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
#         'HOST': os.environ.get('POSTGRES_HOST'),
#         'PORT': '5432'
#         # 'OPTIONS': {'sslmode': 'require'}
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'awtar-backend-db',
        'USER': 'awtaradmin',
        'PASSWORD': 'StrongP@ssword1212',
        'HOST': 'awtar-backend-db.postgres.database.azure.com',
        'PORT': '5432'
        # 'OPTIONS': {'sslmode': 'require'}
    }
}


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_URL = 'Media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 15,
}

# 'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    # ]

if not LOCAL:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, '/static/'),
    ]

    AZURE_ACCOUNT_NAME = os.environ.get('AZURE_ACCOUNT_NAME')
    AZURE_ACCOUNT_KEY = os.environ.get('AZURE_ACCOUNT_KEY')
    AZURE_LOCATION = os.environ.get('AZURE_LOCATION')
    AZURE_CONTAINER = os.environ.get('AZURE_CONTAINER')
    AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'

    STATIC_LOCATION = 'static'
    STATIC_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'

    STATICFILES_STORAGE = 'storages.backends.azure_storage.AzureStorage'
    DEFAULT_FILE_STORAGE = 'core.custom_storage.AzureMediaStorage'