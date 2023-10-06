from django.test import TestCase, Client
from django.urls import reverse
from forum.models import Topic
from forum import views
from django.contrib.auth.models import User
from users.models import UserProfile

class TestViews(TestCase):

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

    def test_home_GET(self):

        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/home.django-html')
    
    def test_topic_GET(self):

        response = self.client.get(self.topic_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/topic.django-html')

    def test_new_topic_POST(self):

        response = self.client.post(self.new_topic_url, {
            'author': self.test_user,
            'name': 'post test',
            'description': 'post description'
        })

        # the view redirects on success
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Topic.objects.get(slug='post-test').name, 'post test')

    
    def test_new_topic_POST_logged_out(self):
        self.client.logout()

        response = self.client.post(self.new_topic_url, {
            'author': self.test_user,
            'name': 'post test',
            'description': 'post description'
        })

        # the view redirects on success
        self.assertEquals(response.status_code, 302)
        # self.assert(Topic.objects.get(slug='post-test').name, 'post test')
        with self.assertRaises(Topic.DoesNotExist):
            Topic.objects.get(slug='post-test')
    
    def test_new_topic_POST_no_data(self):

        response = self.client.post(self.new_topic_url)

        # the view redirects on success
        self.assertEquals(response.status_code, 200)
        # no new topic added so only 1 exists
        self.assertEquals(Topic.objects.count(), 1)

    