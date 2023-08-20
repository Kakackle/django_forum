from django.shortcuts import render, redirect, get_list_or_404
from django.urls import reverse
from . import models
from django.contrib.auth.models import User

from .forms import NewTopicForm, NewThreadForm

# Create your views here.
# TODO:
# create post view + edit + delete
# tak samo thread i topic
# user view
# login, register etc

# home with topic boards to choose from
def home_view(request):
    topics = list(models.Topic.objects.all())
    context = {'topics': topics}
    
    return render(request, "forum/home.django-html", context)

def about_view(request):
    context = {'links': [
                   {
                       'name': 'About',
                       'link': reverse('forum:about')
                   }
               ]}
    return render(request, "forum/about.django-html",
           context)

def topic_view(request, topic_slug):
    topic = models.Topic.objects.get(slug=topic_slug)
    link_string = reverse('forum:topic', kwargs={'topic_slug':topic_slug})
    threads = list(topic.threads.all())

    links = [{
        'name': topic.name,
        'link': link_string
    }]
    context = {'topic': topic,
               'links': links,
               'threads': threads}
    return render(request, "forum/topic.django-html", context)

def add_topic_view(request):
    pass


def thread_view(request, topic_slug, thread_slug):
    topic = models.Topic.objects.get(slug=topic_slug)
    topic_link_string = reverse('forum:topic', kwargs={'topic_slug':topic_slug})
    thread = models.Thread.objects.get(slug=thread_slug)
    thread_link_string = reverse('forum:thread', kwargs={'topic_slug':topic_slug, 'thread_slug': thread_slug})
    posts = list(thread.posts.all())
    print(posts[0].author.profile.bio)

    links = [{
        'name': topic.name,
        'link': topic_link_string
        },
        {
        'name': thread.name,
        'link': thread_link_string
        }
        ]
    context = {'thread': thread,
               'links': links,
               'posts': posts
               }
    return render(request, "forum/thread.django-html", context)

def new_topic(request):
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        user = User.objects.first()

        if form.is_valid():
            topic = form.save(commit=False)
            #wlasne pole, z modelu z related field
            topic.author = user
            topic.save()
            return redirect('forum:home')
    else:
        form = NewTopicForm()
    return render(request, 'forum/new_topic_form_crispy.django-html', {'form': form})

def new_thread(request, topic_slug):
    topic = models.Topic.objects.get(slug=topic_slug)
    user = User.objects.first()
    if request.method == 'POST':
        form = NewThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            #wlasne pola, z modelu z related field
            thread.author = user
            thread.topic = topic
            thread.save()

            #dodatkowo tworzony initial obiekt post w thread
            post = models.Post.objects.create(
                author = user,
                content = form.cleaned_data.get('content'),
                thread=thread
            )
            return redirect('forum:thread', topic_slug=topic_slug, thread_slug=thread.slug)
    else:
        form = NewThreadForm()
    return render(request, 'forum/new_thread.django-html', {'form': form})
