# from django.conf import settings
# settings.configure()

from django.contrib.auth.models import User
from forum.models import Topic, Thread, Post

user = User.objects.first()

topic = Topic.objects.get(slug='programming-general')

for i in range(10):
    name = 'thread test #{}'.format(i)
    thread = Thread.objects.create(name=name, topic=topic, author=user)
    Post.objects.create(content='Lorem ipsum...', thread=thread, author=user)