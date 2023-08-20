from django.shortcuts import render, redirect, get_list_or_404
from django.urls import reverse
from . import models
from django.contrib.auth.models import User

from .forms import NewTopicForm

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
        name = request.POST['name']
        desc = request.POST['desc']

        user = User.objects.first()

        topic = models.Topic.objects.create(
            name=name,
            description=desc,
            author=user
        )

        return redirect('forum:home')
    
    return render(request, 'forum/new_topic.django-html')


def new_topic_form(request):

    if request.method == 'POST':
        # name = request.POST['name']
        # desc = request.POST['desc']

        form = NewTopicForm(request.POST)
        user = User.objects.first()

        if form.is_valid():
            # dodawanie samo 
            # topic = form.save()
            
            # tutaj dodawanie dodatkowych pol typu related
            topic = form.save(commit=False)
            topic.author = user
            topic.save()


        # topic = models.Topic.objects.create(
        #     name=name,
        #     description=desc,
        #     author=user
        # )

            return redirect('forum:home')
    else:
        form = NewTopicForm()
    # TODO: dodaj html ktory by przyjmowal form i wyswietlal z:
    # https://simpleisbetterthancomplex.com/series/2017/09/18/a-complete-beginners-guide-to-django-part-3.html
    return render(request, 'forum/new_topic_form.django-html', {'form': form})