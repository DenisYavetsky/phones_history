from django.contrib import admin
from django.urls import path
from custom_users.views import auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', auth, name='auth'),
]
