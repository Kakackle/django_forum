from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.views.generic import UpdateView
from .models import UserProfile
from django.views.decorators.cache import cache_page

# Create your views here.

import logging
logger = logging.getLogger('user')

# cache for 5 minutes
# @cache_page(60*5)
def user_view(request, user_slug):
    try:
        user = get_object_or_404(User, username=user_slug)
    except Http404:
        return redirect('forum:home')
    context={'user': user}
    return render(request, "users/user.django-html", context)

@method_decorator(login_required, name='dispatch')
class UserProfileUpdateView(UpdateView):
    model = UserProfile
    fields = ('profile_img', 'bio')
    template_name = 'users/profile_edit.django-html'
    slug_url_kwarg = 'user_slug'
    context_object_name = 'profile'
    # success_url = reverse('users:user', kwargs={'user_slug': model.slug})

    # def get_object(self):
    #     return UserProfile.objects.get(slug=self.request.user.username)
    
    def form_valid(self, form):
        profile = form.save()
        return redirect('users:user', user_slug=profile.slug)