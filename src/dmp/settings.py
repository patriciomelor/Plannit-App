import os
from pathlib import Path
from django.urls import reverse_lazy
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zes0))g)ouv+_he(zl)(8*@+(l$vn$p+4$ue$&2gp=(wu2na11'

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
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'import_export',
    'crispy_forms',    
    # 'easy_thumbnails',
    # 'filer',
    # 'mptt',
    # 'multiupload',
    'django_filters',
    'formtools',
    'rest_framework',
    'rest_framework.authtoken',
    'invitations',
    'django_summernote',
    
    'dashboard',
    'tools',
    'notifications',
    'panel_carga',
    'bandeja_es',
    'configuracion',
    'buscador',
    'status',
    'status_encargado',
    'analitica',
    

]

# AUTH_USER_MODEL = 'dashboard.Usuario'

SITE_ID = 3

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Allauth methods
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_EMAIL_VERIFICATION = False
ACCOUNT_SIGNUP_FORM_CLAS = 'dashboard.forms.CrearUsuario'

#Invitation methods
#ACCOUNT_ADAPTER = 'configuracion.adapters.AccountAdapter'
ACCOUNT_ADAPTER = 'invitations.models.InvitationsAdapter'
INVITATIONS_ACCEPT_INVITE_AFTER_SIGNUP = True

LOGIN_URL = reverse_lazy("account_login")

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

APPEND_SLASH = False

# REST Framework

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dmp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.joinpath('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',                
            ],
        },
    },
]

# EMAIL SETTINGS

EMAIL_HOST = 'mail.stod.cl'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'dmp@stod.cl'
EMAIL_HOST_PASSWORD = 'dmp.2020'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'dmp@stod.cl'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


WSGI_APPLICATION = 'dmp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dmpdb5',
        'USER': 'postgres',
        'PASSWORD': 'dmp.2020',
        'HOST': '134.209.78.27',
        'PORT': 5432,
        'SSLMODE': 'require',
        'DISABLE_SERVER_SIDE_CURSORS': True,
    }
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

LANGUAGE_CODE = 'es'
_ = lambda s: s

LANGUAGES = (
 ('es', _('Espanish')),
 ('zh', _('Chinese')),
 ('en', _('English')),
)
TIME_ZONE = 'UTC'  # use this, whenever possible
TIME_ZONE = 'America/Santiago'


USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (str(BASE_DIR.joinpath('static')),)
STATIC_ROOT = STATIC_ROOT = str(BASE_DIR.joinpath('staticfiles'))
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

MEDIA_ROOT = os.path.join(BASE_DIR,'static/media')

MEDIA_URL = '/media/'

MESSAGE_TAGS = {
    messages.DEBUG: 'alert alert-bordered alert-info',
    messages.INFO: 'alert alert-bordered alert-info',
    messages.SUCCESS: 'alert alert-bordered alert-success',
    messages.WARNING: 'alert alert-bordered alert-warning',
    messages.ERROR: 'alert alert-bordered alert-warning',

}
#summernote
SUMMERNOTE_CONFIG = {
    # Using SummernoteWidget - iframe mode, default
    'iframe': False,

    # You can put custom Summernote settings
    'summernote': {
        # As an example, using Summernote Air-mode
        'airMode': False,

        # Change editor size
        'width': '100%',
        'height': '480',

        # Use proper language setting automatically (default)
        'lang': 'es-ES',

        # Toolbar customization
        # https://summernote.org/deep-dive/#custom-toolbar-popover
        'toolbar': [
            ['style', ['style']],
            ['font', ['bold', 'underline', 'clear']],
            ['fontname', ['fontname']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['table', ['table']],
            ['view', ['fullscreen', 'codeview', 'help']],
        ],


        # You can also add custom settings for external plugins
        'print': {
            'stylesheetUrl': '/some_static_folder/printable.css',
        },
        'codemirror': {
            'mode': 'htmlmixed',
            'lineNumbers': 'true',
            # You have to include theme file in 'css' or 'css_for_inplace' before using it.
            'theme': 'monokai',
        },
    },

    # Require users to be authenticated for uploading attachments.
    'attachment_require_authentication': True,

    # You can completely disable the attachment feature.
    'disable_attachment': False,

    # Set to `True` to return attachment paths in absolute URIs.
    'attachment_absolute_uri': False,


}