from django.contrib.admin import register, ModelAdmin
from .models import Device


@register(Device)
class DeviceAdmin(ModelAdmin):
    list_display: list[str] = ['id', 'name', 'state', 'pin']
