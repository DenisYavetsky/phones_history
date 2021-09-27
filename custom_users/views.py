from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import *


def auth(request):
    user = get_object_or_404(CustomUsers, user_login='qwerty')
    return HttpResponse(user.check_password('qwerty'))
