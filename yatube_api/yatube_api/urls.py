from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect
from rest_framework.authtoken.views import obtain_auth_token

def redirect_to_api(request):
    return redirect('/api/v1/')

urlpatterns = [
    path('', redirect_to_api),
    path('admin/', admin.site.urls),
    path('api/v1/api-token-auth/', obtain_auth_token),  
    path('api/v1/', include('api.urls')),  
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
