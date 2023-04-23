from django.contrib.admin import ModelAdmin, register
from .models import AccessKey, UserDevice


@register(AccessKey)
class AccessKeyAdmin(ModelAdmin):
    list_display: tuple[str, ...] = ['id', 'access_to', 'access_link', 
                                 'expire', 'created', 'is_active']
    
    list_filter: tuple[str, ...] = ('created', 'is_active')
    search_fields: tuple[str, ...] = ('access_to',)
    ordering: tuple[str, ...] = ('-created',)

    def access_link(self, obj: AccessKey) -> str:
        return f'127.0.0.1:8000/Access-Link/{obj.key}'


@register(UserDevice)
class UserDeviceAdmin(ModelAdmin):
    list_display: tuple[str, ...] = ['id', 'device_id', 'access_key', 
                                 'created', 'last_activity', 'last_activity_ip', 
                                 'is_active']
    
    list_filter: tuple[str, ...] = ('created', 'is_active')
    search_fields: tuple[str, ...] = ('access_to',)
    ordering: tuple[str, ...] = ('-created',)

