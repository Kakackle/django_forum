from django.test import SimpleTestCase
from django.urls import reverse, resolve
from forum import views
class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('forum:home')
        self.assertEquals(resolve(url).func, views.home_view)
    
    def test_about_url_is_resolved(self):
        url = reverse('forum:about')
        self.assertEquals(resolve(url).func, views.about_view)
        # for class-based views it would be .func.view_class

    def test_new_topic_url_is_resolved(self):
        url = reverse('forum:new_topic')
        self.assertEquals(resolve(url).func, views.new_topic)

    def test_topic_url_is_resolved(self):
        url = reverse('forum:topic', args=['some-slug'])
        self.assertEquals(resolve(url).func, views.topic_view)