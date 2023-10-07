import factory
from faker import Faker
fake = Faker()

from django.contrib.auth.models import User
from forum.models import Topic, Thread

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = fake.name()
    is_staff = 'True'

class TopicFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Topic
    
    name = 'django'
    description = 'django topic desc'
    author = factory.SubFactory(UserFactory)


class ThreadFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Thread
    
    name = 'first thread'
    topic = factory.SubFactory(TopicFactory)