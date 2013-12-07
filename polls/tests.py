"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import datetime
import time
from django.utils import timezone

from django.test import TestCase
import nose.tools as nt

from polls.models import *

from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
        
class TestPoll(object):
    def test_was_published_recently_with_future_poll(self):
        """
        was_published_recently() should return False for polls whose pub_date is in the future
        """
        future_poll = Poll(pub_date=timezone.now() + datetime.timedelta(days=30))
        nt.assert_equal(future_poll.was_published_recently(),True)


class BaseTestCase(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriver()
        super(BaseTestCase, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(BaseTestCase, cls).tearDownClass()
        cls.driver.quit()

class PollsTestCase(BaseTestCase):

    def test_vote(self):
        self.driver.get(self.live_server_url + '/polls/')
        poll = self.driver.find_element_by_link_text('ShiningPanda is a...')
        poll.click()
        time.sleep(2)    # Should use accurate WebDriverWait
        choices = self.driver.find_elements_by_name('choice')
        self.assertEquals(3, len(choices))
        choices[2].click()
        choices[2].submit()
        lis = self.driver.find_elements_by_tag_name('li')
        self.assertEquals(3, len(lis))
        self.assertEquals('Hosted CI service? -- 0 votes', lis[0].text)
        self.assertEquals('Consulting firm? -- 0 votes', lis[1].text)
        self.assertEquals('Both! -- 1 vote', lis[2].text)
