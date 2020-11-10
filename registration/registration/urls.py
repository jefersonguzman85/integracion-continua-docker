from django.contrib import admin
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()

urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls')),
]
