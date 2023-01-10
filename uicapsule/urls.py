"""uicapsule URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('cms/', admin.site.urls),
    path("", include("core.urls"))
]
