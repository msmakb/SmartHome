from uuid import uuid4
from dataclasses import dataclass
from random import randrange

from django.http import HttpRequest


@dataclass
class UserData:
    username: str
    password: str
    device_id: str


def generateUserData() -> UserData:
    device_id: str = str(uuid4())
    return UserData(
        f"{device_id.rsplit('-', maxsplit=1).pop().upper()}",
        f"{str(uuid4()).rsplit('-', maxsplit=1).pop().upper()}",
        device_id.replace('-', str(randrange(0, 9))),
    )


def getClientIp(request: HttpRequest) -> str:
    http_x_forwarded_for: str = request.META.get('HTTP_X_FORWARDED_FOR')
    if http_x_forwarded_for:
        ip: str = http_x_forwarded_for.split(',')[0]
    else:
        ip: str = request.META.get('REMOTE_ADDR')
    return ip


def getUserAgent(request: HttpRequest) -> str:
    if request.META.get('HTTP_USER_AGENT'):
        return request.META.get('HTTP_USER_AGENT')
    return request.headers.get('User-Agent', 'Unknown')
