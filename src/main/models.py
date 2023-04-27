from typing import Any
from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import datetime, timedelta, now

from . import constant


class AccessKey(models.Model):
    access_to: str = models.CharField(max_length=50, blank=True, null=True)
    access_period: str = models.CharField(max_length=2, default=constant.ACCESS_PERIOD.ONE_MONTH, 
                                          choices=constant.CHOICES.ACCESS_PERIOD)
    key = models.CharField(max_length=40, unique=True, editable=False, blank=True, null=True)
    created: datetime = models.DateTimeField(auto_now_add=True)
    expire: datetime = models.DateTimeField(editable=False, blank=True, null=True)
    is_active: bool = models.BooleanField(editable=False, default=False)

    def __str__(self) -> str:
        return self.access_to
    
    def getAccessPeriodInSeconds(self) -> int:
        # Python 3.10+
        # match self.access_period:
        #     case constant.ACCESS_PERIOD.ONE_DAY:
        #         return 86_400
        #     case constant.ACCESS_PERIOD.THREE_DAYS:
        #         return 259_200
        #     case constant.ACCESS_PERIOD.ONE_WEEK:
        #         return 604_800
        #     case constant.ACCESS_PERIOD.TWO_WEEKS:
        #         return 1_209_600
        #     case constant.ACCESS_PERIOD.ONE_MONTH:
        #         return 2_592_000
        #     case constant.ACCESS_PERIOD.THREE_MONTHS:
        #         return 7_776_000
        #     case constant.ACCESS_PERIOD.ONE_YEAR:
        #         return 31_536_000

        # Python 3.9-
        if constant.ACCESS_PERIOD.ONE_DAY:
            return 86_400
        elif constant.ACCESS_PERIOD.THREE_DAYS:
            return 259_200
        elif constant.ACCESS_PERIOD.ONE_WEEK:
            return 604_800
        elif constant.ACCESS_PERIOD.TWO_WEEKS:
            return 1_209_600
        elif constant.ACCESS_PERIOD.ONE_MONTH:
            return 2_592_000
        elif constant.ACCESS_PERIOD.THREE_MONTHS:
            return 7_776_000
        elif constant.ACCESS_PERIOD.ONE_YEAR:
            return 31_536_000
            
    def save(self, *args: list[Any], **kwargs: dict[str, Any]) -> None:
        if self.pk:
            return super().save(*args, **kwargs)
        
        if not self.access_to or self.access_to.isspace():
            self.access_to = constant.UNSPECIFIED

        self.key = str(uuid4())
        self.expire = now() + timedelta(minutes=constant.ACCESS_KEY_EXPIRE_MINUTES)
        self.is_active = True
        return super().save(*args, **kwargs)


class UserDevice(models.Model):
    user: User = models.ForeignKey(User, on_delete=models.CASCADE)
    user_agent: str = models.CharField(max_length=256, null=True, blank=True)
    device_id: str = models.CharField(max_length=40, unique=True)
    access_key: AccessKey = models.ForeignKey(AccessKey, on_delete=models.CASCADE)
    created: datetime = models.DateTimeField(auto_now_add=True)
    last_activity: datetime = models.DateTimeField(auto_now=True)
    last_activity_ip: str = models.GenericIPAddressField()
    last_activity_log: str = models.CharField(max_length=256, null=True, blank=True)
    is_active: bool = models.BooleanField(default=True)

    def __str__(self) -> str:
        if self.access_key.access_to != constant.UNSPECIFIED:
            return self.access_key.access_to
        else:
            self.user.username

    def logActivity(self, activity: str) -> None:
        fixed_separator: str = ', '
        last_activity_log: str = self.last_activity_log + fixed_separator + activity
        while len(last_activity_log) > 255:
            temp: list[str] = last_activity_log.split(fixed_separator)
            last_activity_log = ''
            for i in temp[1:]:
                if i:
                    last_activity_log += i + fixed_separator
            else:
                last_activity_log = last_activity_log[:-2]

        self.last_activity_log = last_activity_log
        self.save()


    def isDeviceCookieExpired(self) -> bool:
        expire_time: datetime = self.access_key.created \
            + timedelta(seconds=self.access_key.getAccessPeriodInSeconds())
        
        if expire_time < now():
            return True
        return False
