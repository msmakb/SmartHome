from core.settings.config import *
from main.constant import _base_dir

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Database
if PRODUCTION:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': CONFIG['DB_NAME'],
            'USER': CONFIG['DB_USER'],
            'PASSWORD': CONFIG['DB_PASS'],
            'HOST': CONFIG['DB_HOST'],
            'PORT': CONFIG['DB_PORT'],
        }
    }
else:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': _base_dir / 'db.sqlite3',
    }
}
