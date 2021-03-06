from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '7k0^pwc%q2&^t#nan4__fly2gq+y^k*6o9ypc4=dgp^8$otxip'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Django apps
    'apps.commons',
    'apps.tags',
    'apps.users',
    'apps.pages',
    'apps.seo',
    'apps.settings',

    # Other apps
    'sorl.thumbnail',

]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'system.urls'

# Настройки связанные с пользователем
AUTH_USER_MODEL = 'users.User'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'system.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_db',
        'USER': 'tester',
        'PASSWORD': 'testArt',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
password_validation = 'django.contrib.auth.password_validation'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': password_validation + '.UserAttributeSimilarityValidator',
    },
    {
        'NAME': password_validation + '.MinimumLengthValidator',
    },
    {
        'NAME': password_validation + '.CommonPasswordValidator',
    },
    {
        'NAME': password_validation + '.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = False

USE_L10N = False

USE_TZ = False

STATIC_URL = "/static/"
MEDIA_URL = "/media/"

if DEBUG:
    import mimetypes
    mimetypes.add_type("application/javascript", ".js", True)
    STATICFILES_DIRS = [
        BASE_DIR / 'static'
    ]
    INSTALLED_APPS += [
        'debug_toolbar',
    ]
    MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')

    INTERNAL_IPS = [
        '127.0.0.1',
    ]
else:
    # Работает ток на проде
    STATIC_ROOT = BASE_DIR / "static"

MEDIA_ROOT = BASE_DIR / ".." / "media"
# Пока что будет писать в консоль
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'