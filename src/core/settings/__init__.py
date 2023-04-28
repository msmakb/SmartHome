from core.settings.base import *
from core.settings.config import *
from core.settings.db import *
from core.settings.log import *
from core.settings.urls import *

# Version
PROJECT_VERSION = '1.0.0'

# Internationalization
WSGI_APPLICATION = 'core.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Aden'

USE_I18N = True

USE_TZ = True

DEBUG = not PRODUCTION

SECRET_KEY = CONFIG['SECRET_KEY']
