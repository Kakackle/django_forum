from selenium import webdriver
from selenium.webdriver.common.by import By
from forum.models import Topic
from django.contrib.staticfiles.testing import StaticLiveServerTestCase, LiveServerTestCase
from django.urls import reverse
import time

class TestForumHomePage(LiveServerTestCase):

    # def test_foo(self):
    #     self.assertEquals(0, 1)
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.close()

    def test_home_search_is_displayed(self):
        self.browser.get(self.live_server_url)
        
        alert = self.browser.find_element(By.CLASS_NAME, 'label-div')
        self.assertEquals(
            alert.find_element(By.TAG_NAME, 'label').text,
            'Search for a topic:'
        )

    def test_home_create_topic_button_redirects_to_add_topic(self):
        self.browser.get(self.live_server_url)

        new_topic_url = self.live_server_url + reverse('forum:new_topic')

        self.browser.find_element(By.CLASS_NAME, "add-link").click()
       

        self.assertEquals(
            self.browser.current_url,
            new_topic_url
        )