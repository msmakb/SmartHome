from django.urls import path

from . import views
from .constant import PAGES

urlpatterns = [
    path('', views.index, name=PAGES.INDEX),
    path('Access-Link/<str:key>', views.accessKey, name=PAGES.ACCESS_LINK),
]
