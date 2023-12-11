from .settings import *
import environ

ALLOWED_HOSTS = ['charactercreator.us', 'www.charactercreator.us']
DEBUG=False

STATIC_ROOT = '/home/hjriebe/charactercreator.us/public/static/'
MEDIA_ROOT = '/home/hjriebe/charactercreator.us/public/media/'


env = environ.Env()
environ.Env.read_env()

DATABASES = {
    'default': {
	'ENGINE': 'django.db.backends.mysql',
    'NAME': env('DATABASE_NAME'),
    'USER': env('DATABASE_USER'),
    'PASSWORD': env('DATABASE_PASSWORD'),
	'HOST': 'mysql.charactercreator.us',
	'PORT': '3306',
    }
}

EMAIL_HOST_PASSWORD = env('SENDGRID_API_KEY')