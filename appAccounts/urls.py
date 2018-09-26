from django.urls import path

from appAccounts.views import GoogleLogin

urlpatterns = [
    path('', GoogleLogin.as_view(), name='google_login')
]
