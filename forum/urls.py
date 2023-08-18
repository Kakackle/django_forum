from django.urls import path
from . import views

app_name="forum"
urlpatterns = [
    path("home", views.home_view, name="home"),
    path("about", views.about_view, name="about"),
    path("<slug:topic_slug>", views.topic_view, name="topic"),
    path("<slug:topic_slug>/edit", views.topic_view, name="topic_edit"),
    path("<slug:topic_slug>/delete", views.topic_view, name="topic_delete"),
    path("add_topic", views.add_topic_view, name="add_topic")
]
