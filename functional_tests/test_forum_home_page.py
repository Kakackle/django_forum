from selenium import webdriver
from forum.models import Topic
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time

class TestForumHomePage(StaticLiveServerTestCase):

    # def test_foo(self):
    #     self.assertEquals(0, 1)
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.close()

    def test_home(self):
        self.browser.get(self.live_server_url)
        time.sleep(20)