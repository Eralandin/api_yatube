from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/v1/api-token-auth/', obtain_auth_token),
]