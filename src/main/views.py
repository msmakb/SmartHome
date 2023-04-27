from time import sleep

from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone

from pi.models import Device
from pi.PiFunc.devices import MainDoor

from . import constant
from .models import AccessKey, UserDevice
from .util import UserData, generateUserData, getClientIp, getUserAgent


def index(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        user_device: UserDevice = get_object_or_404(
            UserDevice,
            device_id=request.COOKIES.get('device_id')
        )

        if 'Open-Main-Door' in request.POST:
            device: Device = Device.objects.get(name='Main Door')
            main_door: MainDoor = MainDoor(device)
            main_door.open()
            main_door.cleanup()
            user_device.logActivity(
                constant.ACTIVITY_LOG.OPEN_MAIN_GATE)

    return render(request, "index.html", {})

def accessKey(request: HttpRequest, key: str) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect("index")
    
    access_key: AccessKey = get_object_or_404(AccessKey, key=key)
    if not access_key.is_active:
        raise Http404
    
    if access_key.expire < timezone.now():
        access_key.is_active = False
        access_key.save()
        raise Http404
    
    user_data: UserData = generateUserData()

    user: User = User.objects.create_user(
        username=user_data.username,
        password=user_data.password,
        first_name=access_key.access_to
    )

    UserDevice.objects.create(
        user=user,
        user_agent=getUserAgent(request),
        device_id=user_data.device_id,
        access_key=access_key,
        last_activity_ip=getClientIp(request),
        last_activity_log=constant.ACTIVITY_LOG.ACCESS_TOKEN
    )

    login(request, user)
    access_key.is_active = False
    access_key.save()
    response = redirect('index')
    response.set_cookie(
        'device_id', 
        user_data.device_id, 
        max_age=access_key.getAccessPeriodInSeconds()
    )
    return response
