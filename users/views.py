from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.models import User

# Create your views here.

def user_view(request, user_slug):
    try:
        user = get_object_or_404(User, username=user_slug)
    except Http404:
        return redirect('forum:home')
    context={'user': user}
    return render(request, "users/user.django-html", context)