from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import RequestFactory


class {{ app_name|capfirst}}URLTests(TestCase):
    """Tests that every configured URL resolves as expected"""
    pass


class {{ app_name|capfirst}}ManagerTests(TestCase):
    """Tests custom manager methods return querysets as expected"""
    pass


class {{ app_name|capfirst}}ModelTests(TestCase):
    """Tests model methods"""
    pass


class {{ app_name|capfirst}}FormTests(TestCase):
    """Tests forms validation and custom methods"""
    pass


class {{ app_name|capfirst}}ViewTests(TestCase):
    """Tests that views return expected responses"""
    pass
