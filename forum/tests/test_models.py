from django.test import TestCase, Client
from django.urls import reverse
from forum.models import Topic
from forum import views
from django.contrib.auth.models import User
from users.models import UserProfile
class TestModels(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('forum:home')

        self.test_user = User.objects.create(username="test", password="adminadmin")
        self.test_user.set_password('123')
        self.test_user.save()
        
        self.test_profile = UserProfile.objects.create(user=self.test_user)
        self.test_topic = Topic.objects.create(author=self.test_user, name="test topic",
                                                      description="test description")

        logged_user = self.client.login(username="test", password="123")

        self.topic_url = reverse('forum:topic', args=['test-topic'])
        self.new_topic_url = reverse('forum:new_topic')

    def test_topic_slug_changes_at_save(self):
        self.assertEquals(Topic.objects.first().slug, 'test-topic')