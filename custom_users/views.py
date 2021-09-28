from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import *


def auth(request):
    return render(request, 'custom_users/auth.html', context={})
