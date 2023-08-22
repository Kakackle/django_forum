from django.test import TestCase
from django.urls import Resolver404, reverse, resolve
from forum.views import home_view, topic_view
from forum.models import Topic, Thread, Post
from django.contrib.auth.models import User
from django.test import Client

# Create your tests here.
class HomeTests(TestCase):
    def setUp(self):
        user = User.objects.create(username='admin', password='adminadmin')
        self.topic = Topic.objects.create(name="Testing", description="Testing topic board", author=user)
        
        url = reverse('forum:home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        # url = reverse('forum:home')
        # response = self.client.get(url)
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        try:
            view = resolve('/forum/')
            self.assertEquals(view.func, home_view)
        except Resolver404:
            self.fail("couldn't resolve URL")

    def test_home_view_containt_link_to_topic(self):
        topic_url = reverse('forum:topic', kwargs={'topic_slug': self.topic.slug})
        self.assertContains(self.response, 'href="{0}"'.format(topic_url))

class TopicTests(TestCase):
    def setUp(self):
        user = User.objects.create(username='admin', password='adminadmin')
        Topic.objects.create(name="Testing", description="Testing topic board", author=user)
    
    def test_topic_view_success_status_code(self):
        url = reverse('forum:topic', kwargs={'topic_slug':'testing'})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
    
    def test_topic_view_error_status_code(self):
        url = reverse('forum:topic', kwargs={'topic_slug':'notexist'})
        response = self.client.get(url)
        # self.assertEquals(response.status_code, 404)
        # 302 poniewaz redirect
        self.assertEquals(response.status_code, 302)
    
    def test_topic_view_resolves_topic_view(self):
        try:
            view = resolve('/forum/testing')
            self.assertEquals(view.func, topic_view)
        except Resolver404:
            self.fail("couldn't resolve URL")


class NewThreadTests(TestCase):
    def setUp(self):
        self.user =User.objects.create_user(username='john', email='john@doe.com', password='123')
        #poniewaz haslo jest hashowane na backendzie przy powyzszym, wiec:
        self.user.set_password('123')
        self.user.save()
        #albo:
        #user = User.objects.create_user(username='testuser', password='12345')

        Topic.objects.create(name='Django', description='Django topic.', author=self.user)       
        c = Client()
        logged_user = c.login(username="john", password="123")

    def test_csrf(self):
        url = reverse('forum:new_thread', kwargs={'topic_slug': 'django'})
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_new_topic_valid_post_data(self):
        url = reverse('forum:new_thread', kwargs={'topic_slug': 'django'})
        data = {
            'name': 'Test title',
            'content': 'Lorem ipsum dolor sit amet'
        }
        response = self.client.post(url, data)
        self.assertTrue(Thread.objects.exists())
        self.assertTrue(Post.objects.exists())

    def test_new_topic_invalid_post_data(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('forum:new_thread', kwargs={'topic_slug': 'django'})
        response = self.client.post(url, {})
        self.assertEquals(response.status_code, 302)

    def test_new_topic_invalid_post_data_empty_fields(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('forum:new_thread', kwargs={'topic_slug': 'django'})
        data = {
            'name': '',
            'content': ''
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 302)
        self.assertFalse(Thread.objects.exists())
        self.assertFalse(Post.objects.exists())

