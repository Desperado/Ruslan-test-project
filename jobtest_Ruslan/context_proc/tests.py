from tddspry.django import HttpTestCase

from django.template.context import RequestContext
from django.http import HttpRequest

class TestContextProcessor(HttpTestCase):
    def test_context_settings(self):
        """
        Test if django.settings are present in RequestContext
        """
        RequestContext(HttpRequest())
        self.ok_("settings" in RequestContext(HttpRequest()),
                 msg = "There is no 'django.settings' in RequestContext")

