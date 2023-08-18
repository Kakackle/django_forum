from django.urls import path
from . import views

app_name="forum"
urlpatterns = [
    path("home", views.home_view, name="home"),
    path("about", views.about_view, name="about"),
    #user
    path("user/<slug:user_slug>", views.user_view, name="user"),
    # topic
    path("<slug:topic_slug>", views.topic_view, name="topic"),
    path("<slug:topic_slug>/edit", views.topic_view, name="topic_edit"),
    path("<slug:topic_slug>/delete", views.topic_view, name="topic_delete"),
    path("create", views.add_topic_view, name="create_topic"),
    # thread
    path("<slug:topic_slug>/<slug:thread_slug>", views.thread_view, name="thread"),
    path("<slug:topic_slug>/<slug:thread_slug>/edit", views.topic_view, name="thread_edit"),
    path("<slug:topic_slug>/<slug:thread_slug>/delete", views.topic_view, name="thread_delete"),
    path("<slug:topic_slug>/create", views.topic_view, name="create_thread"),
    # post
    path("<slug:topic_slug>/<slug:thread_slug>/post", views.topic_view, name="create_post"),
    path("<slug:topic_slug>/<slug:thread_slug>/<slug:post_slug>/edit", views.topic_view, name="edit_post"),
    path("<slug:topic_slug>/<slug:thread_slug>/<slug:post_slug>/delete", views.topic_view, name="delete_post"),

]

# TODO: co z edytowaniem u usuwaniem postow
# TODO: rozdzielenie users na oddzielny app - ten zwiazany jest z forum a users to cos oddzielnego?
