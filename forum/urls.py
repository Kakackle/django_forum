from django.urls import path
from . import views

app_name="forum"
urlpatterns = [
    path("", views.home_view, name="home"),
    path("about", views.about_view, name="about"),
    # topic
    path("new_topic", views.new_topic, name="new_topic"),
    path("<slug:topic_slug>", views.topic_view, name="topic"),
    # path("<slug:topic_slug>/edit", views.topic_view, name="topic_edit"),
    # path("<slug:topic_slug>/delete", views.topic_view, name="topic_delete"),
    # thread
    path("<slug:topic_slug>/new_thread", views.new_thread, name="new_thread"),
    path("<slug:topic_slug>/<slug:thread_slug>", views.thread_view, name="thread"),
    # path("<slug:topic_slug>/<slug:thread_slug>/edit", views.topic_view, name="thread_edit"),
    # path("<slug:topic_slug>/<slug:thread_slug>/delete", views.topic_view, name="thread_delete"),
    # post
    path("<slug:topic_slug>/<slug:thread_slug>/post", views.new_post, name="new_post"),
    # path("<slug:topic_slug>/<slug:thread_slug>/", views.topic_view, name="create_post"),
    path("<slug:topic_slug>/<slug:thread_slug>/<slug:post_slug>/edit", views.PostUpdateView.as_view(), name="edit_post"),
    # path("<slug:topic_slug>/<slug:thread_slug>/<slug:post_slug>/delete", views.topic_view, name="delete_post"),
    path("<slug:topic_slug>/<slug:thread_slug>/<slug:post_slug>/like", views.like_post_view, name="like_post"),
    path("posts/<slug:post_slug>/delete", views.delete_post_view, name="delete_post"),
]

