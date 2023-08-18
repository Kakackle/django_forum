from django.shortcuts import render
from django.urls import reverse
from . import models

# Create your views here.

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