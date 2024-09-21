from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

#DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'dbempleado',
#         'USER': 'udemy',
#         'PASSWORD': 'curso2024',
#         'HOST': 'debian',
#         'PORT': '5432',
#     }
#}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'udemy_django',
#         'USER': 'udemy_django',
#         'PASSWORD': '-.Udemy445Django329.-',
#         'HOST': 'debian',  # O el host donde esté tu servidor MySQL
#         'PORT': '3306',    # Puerto por defecto para MySQL
#     }
# }

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.mysql',
       'NAME': 'mauriciomouatgue$cursos',
       'USER': 'mauriciomouatgue',
       'PASSWORD': 'Nube5Caja',
       'HOST': 'mauriciomouatguerrero.mysql.pythonanywhere-services.com',  # O el host donde esté tu servidor MySQL
       'PORT': '',    # Puerto por defecto para MySQL
   }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'