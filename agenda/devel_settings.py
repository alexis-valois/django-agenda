__author__ = 'Alexis'
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'agenda_dev',
        'USER': 'agenda_dev',
        'PASSWORD': 'agenda_dev',
        'PORT': '5432',
        'HOST': 'localhost',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'