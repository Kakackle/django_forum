from django.urls import path
from . import views

app_name="forum"
urlpatterns = [
    path("home", views.home_view, name="home"),
    path("about", views.about_view, name="about"),
    path("<slug:topic_slug>", views.topic_view, name="topic"),
    path("<slug:topic_slug>/edit", views.topic_view, name="topic_edit"),
    path("<slug:topic_slug>/delete", views.topic_view, name="topic_delete"),
    path("create", views.add_topic_view, name="create_topic"),
    path("<slug:topic_slug>/<slug:thread_slug>", views.thread_view, name="thread"),
    path("<slug:topic_slug>/<slug:thread_slug>/edit", views.topic_view, name="thread_edit"),
    path("<slug:topic_slug>/<slug:thread_slug>/delete", views.topic_view, name="thread_delete"),
    path("<slug:topic_slug>/create", views.topic_view, name="create_thread"),
    path("<slug:topic_slug>/<slug:thread_slug>/post", views.topic_view, name="create_post"),
]

# TODO: co z edytowaniem u usuwaniem postow
