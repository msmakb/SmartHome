from time import sleep

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from pi.PiFunc.devices import LED
from pi.models import Device


def index(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        led = LED(Device.objects.first())

        if 'ON' in request.POST:
            led.on()
        elif 'OFF' in request.POST:
            led.off()
        elif 'BLINK' in request.POST:
            led.blink()

    return render(request, "index.html", {})
