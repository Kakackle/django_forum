from django.urls import path
from . import views

app_name="users"
urlpatterns = [
    #user
    path("<slug:user_slug>", views.user_view, name="user"),
    path("<slug:user_slug>/edit", views.UserProfileUpdateView.as_view(), name="profile_edit")
]