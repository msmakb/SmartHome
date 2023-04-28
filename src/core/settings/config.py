import json

PRODUCTION = False

if PRODUCTION:
    with open('/etc/config.json') as config_file:
        CONFIG = json.load(config_file)
else:
    CONFIG = {
        'SECRET_KEY': 'django-insecure-j*tvdynhq=vlgysivo$vbv(2zgnca3#3$bormyi*pn4(q$&@fn'
    }
