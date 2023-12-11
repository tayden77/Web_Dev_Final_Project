
import environ

ALLOWED_HOSTS = ['charactercreator.us', 'www.charactercreator.us']
DEBUG=False

STATIC_ROOT = '/home/hjriebe/charactercreator.us/public/static/'
MEDIA_ROOT = '/home/hjriebe/charactercreator.us/public/media/'


env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

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

SECRET_KEY = env('SECRET_KEY')

SECURE_HSTS_SECONDS = 360                                                                                       
SECURE_HSTS_PRELOAD = True                                                                                       
SECURE_HSTS_INCLUDE_SUBDOMAINS = True                                                                                       

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True