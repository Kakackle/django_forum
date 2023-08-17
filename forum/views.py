from django.shortcuts import render
from . import models

# Create your views here.

def home_view(request):
    context = {'test': 'test of context'}
    
    return render(request, "forum/home.django-html", context)

def about_view(request):
    context = {'links': [
                   {
                       'name': 'About',
                       'link': 'forum:about'
                    #    'link': "{% url 'forum:about' %}",
                   }
               ]}
    return render(request, "forum/about.django-html",
           context)

def topic_view(request, topic_slug):
    topic = models.Topic.objects.get(slug=topic_slug)
    # link_string = "{% url 'forum:topic' {} %}".format(topic_slug)
    link_string = "forum:topic {}".format(topic_slug)
    print(link_string)
    links = [{
        'name': topic.name,
        'link': link_string
    }]
    context = {'topic': topic,
               'links': links}
    return render(request, "forum/topic.django-html", context)
