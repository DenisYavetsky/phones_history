from django.contrib import admin
from django.urls import path
from custom_users.views import auth
from django.views.static import serve
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', auth, name='auth'),
]
