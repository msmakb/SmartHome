from pathlib import Path
from typing import Final
from collections import namedtuple as _NT

# ------------------------------------ private ------------------------------------ #
_base_dir: Final[Path] = Path(__file__).resolve().parent.parent

# ---------------------------------- public --------------------------------------- #
UNSPECIFIED: Final[str] = 'UNSPECIFIED'
ACCESS_KEY_EXPIRE_MINUTES: Final[int] = 60

ACCESS_PERIOD = _NT('str', [
    'ONE_DAY',
    'THREE_DAYS',
    'ONE_WEEK',
    'TWO_WEEKS',
    'ONE_MONTH',
    'THREE_MONTHS',
    'ONE_YEAR'
])(
    '1D',
    '3D',
    '1W',
    '2W',
    '1M',
    '3M',
    '1Y',
)
ACTIVITY_LOG = _NT('str', [
    'ACCESS_TOKEN',
    'OPEN_MAIN_GATE',
])(
    'Activate access toke',
    'Open main gate',
)

LOGGERS = _NT('str', [
    'MAIN',
    'MIDDLEWARE',
    'MODELS',
])(
    'SmartHome.Main',
    'SmartHome.Middleware',
    'SmartHome.Models',
)

CHOICES = _NT('str', [
    'ACCESS_PERIOD',
])(
    [(access_period, access_period) for access_period in ACCESS_PERIOD]
)

PAGES = _NT('str', [
    'INDEX',
    'ACCESS_LINK',
]
)(
    'index',
    'access-link',
)