from .settings import  INSTALLED_APPS,MIDDLEWARE
INSTALLED_APPS+=['corsheaders']

MIDDLEWARE.insert(0,'django.middleware.common.CommonMiddleware')
MIDDLEWARE.insert(0,'corsheaders.middleware.CorsMiddleware')

CORS_ORIGIN_ALLOW_ALL=True
