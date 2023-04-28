import json

from core.settings.base import *
from core.settings.db import *
from core.settings.log import *
from core.settings.urls import *

# Version
PROJECT_VERSION = '1.0.0'

# Internationalization
WSGI_APPLICATION = 'core.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DEBUG = True

PRODUCTION = False

with open('/etc/config.json') as config_file:
    CONFIG = json.load(config_file)

if PRODUCTION:
    SECRET_KEY = CONFIG['SECRET_KEY']
else:
    SECRET_KEY = 'django-insecure-j*tvdynhq=vlgysivo$vbv(2zgnca3#3$bormyi*pn4(q$&@fn'
