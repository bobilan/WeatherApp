import environ
from .base import *

env = environ.Env()
environ.Env.read_env(str(BASE_DIR / ".env"))

SECRET_KEY = env('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ["*"]

# Check if the DOCKER_CONTAINER environment variable is set
if env.bool('DOCKER_CONTAINER', default=False):
    DB_HOST = 'postgres'
else:
    DB_HOST = 'localhost'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str('DB_NAME'),
        'USER': env.str('DB_USER'),
        'PASSWORD': env.str('DB_PASS'),
        'HOST': DB_HOST,
        'PORT': env.str('DB_PORT'),
    }
}

