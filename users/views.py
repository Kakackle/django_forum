from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def user_view(request, user_slug):
    user = User.objects.get(username=user_slug)
    context={'user': user}
    return render(request, "users/user.django-html", context)