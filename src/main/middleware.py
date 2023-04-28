from logging import getLogger, Logger
from typing import Callable


from django.conf import settings
from django.contrib.auth import logout
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.urls import resolve, reverse

from . import constant
from .models import UserDevice
from .util import getClientIp

logger: Logger = getLogger(constant.LOGGERS.MIDDLEWARE)

class AllowedUserMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response: Callable[[HttpRequest], HttpResponse] = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        response: HttpResponse = self.get_response(request)
        path_name: str = resolve(request.path_info).url_name
        logger.info("Client IP: " + getClientIp(request))
        
        if getClientIp(request) in settings.ALLOWED_HOSTS:
            return response
        
        if path_name == constant.PAGES.ACCESS_LINK:
            return response

        if not request.user.is_authenticated:
            raise Http404

        if not self.isAllowedToAccessAdmin(request):
            raise Http404

        user_device: UserDevice = get_object_or_404(
            UserDevice,
            device_id=request.COOKIES.get('device_id')
        )

        if not user_device.is_active:
            raise Http404
        
        if user_device.isDeviceCookieExpired():
            logout(request)
            user_device.is_active = False
            user_device.save()
            raise Http404

        return response
    
    def isAllowedToAccessAdmin(self, request: HttpRequest) -> bool:
        if request.path.startswith(reverse('admin:index')):
            if request.user.is_superuser:
                return True
            return False
        return True
