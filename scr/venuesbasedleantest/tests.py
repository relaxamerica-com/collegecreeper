from django.test.utils import setup_test_environment
from google.appengine.ext import testbed
from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory, Client

from views import landing


class BasicViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_mail_stub()
        self.testbed.init_memcache_stub()
        setup_test_environment()

    def tearDown(self):
        self.testbed.deactivate()

    def test_landing(self):
        request = RequestFactory().get(reverse('venuesbasedleantest_landing'))
        response = landing(request)
        print(response)