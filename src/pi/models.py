from django.db import models


class Device(models.Model):
    name: str = models.CharField(max_length=30)
    state: str = models.CharField(max_length=1)
    pin: int = models.SmallIntegerField()
