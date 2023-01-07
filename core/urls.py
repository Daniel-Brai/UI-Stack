from django.urls import path
from .views import LandingPage, PrivacyPage

app_name = 'core'

urlpatterns = [
    path("", LandingPage.as_view(), name='landing'),
    path("privacy/", PrivacyPage.as_view(), name='privacy')
]