from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib.auth import login as auth_login

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            #log the created user in
            auth_login(request, user)
            return redirect('forum:home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.django-html', {'form': form})