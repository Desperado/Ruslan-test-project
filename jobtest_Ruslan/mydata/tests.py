#!/usr/bin/python
# -*- coding: utf-8 -*-
# mydata/tests.py
""" Mydata tests """

from tddspry.django import DatabaseTestCase, HttpTestCase
from django.core.urlresolvers import reverse
from models import Mybio
from django.contrib.auth.models import User
from jobtest_Ruslan.test_data import test_account, test_contact, test_profile



class TestFixture(DatabaseTestCase):
    """Methods for testing fixture"""
    def test_admin_user_login(self):
        '''
        Test admin password and login restored from fixture
        '''
        admin = User.objects.get(username=test_account["username"])
        self.ok_(admin.check_password(test_account["password"]))

    def test_my_contact_exists(self):
        """
        Test if data is uploaded from fixture
        """
        self.assert_count(Mybio, 1)
        self.assert_read(Mybio, **test_contact)


class TestContactsViews(HttpTestCase):
    """Methods for testing contacts views"""
    def test_login_required(self):
        '''
        Test if login required on contacts page
        '''
        self.go(reverse("profile-edit", kwargs=test_profile))
        self.find("Login required")

    def test_contacts_view(self):
        """
        Test if contact view contains all relevant data from fixture
        """
        self.login(test_account["username"],
                   test_account["password"], 
                   url=reverse("login") + "?next=" + \
                       reverse("profile",
                               kwargs=test_profile))
        self.find(test_contact["bio"])
        self.find(test_contact["first_name"])
        self.find(test_contact["last_name"])
        self.find(test_contact["contacts"])
        self.go('accounts/logout')

    def test_calendar_widget_present(self):
        """
        Test if calendar widget is loaded
        """
        self.login(test_account["username"],
                   test_account["password"], 
                   url=reverse("login") + "?next=" + \
                       reverse("profile",
                               kwargs=test_profile))
        self.find("/media/js/jquery-1.4.2.min.js")
        self.find("/media/datepicker/datepicker.js")
        self.find("/media/datepicker/css/datepicker.css")
        self.go('accounts/logout')


class TestContactsForm(HttpTestCase):
    """Methods for testing contacts form"""
    def test_contact_edit_form(self):
        '''
        Test contact edit form
        '''
        self.login(test_account["username"],
                   test_account["password"], 
                   url=reverse("login") + "?next=" + \
                       reverse("profile",
                               kwargs=test_profile))
        self.fv("1", "bio", "Who was born January 27?")
        self.fv("1", "first_name", "First Name")
        self.fv("1", "last_name", "Last Name")
        self.fv("1", "contacts", "0987717059, Lviv")
        self.submit()
        self.find("Who was born January 27?")
        self.find("First Name")
        self.find("Last Name")
        self.find("0987717059, Lviv")

    def test_contact_reverse_edit_form(self):
        '''
        Test if contact edit form could be reversed
        '''
        from forms import FormReverse

        class TestFormReverse(FormReverse):
            class Meta:
                model = Mybio
        reverse = TestFormReverse().fields.keys()
        reverse.reverse()
        self.ok_(TestFormReverse(reverse=True).fields.keys() == reverse)


class TestTemplatetags(HttpTestCase):
    """Methods for testing template tags"""
    def test_edit_list_tag(self):
        '''
        Test 'edit_list' tag
        '''
        from django.template import Context, Template
        template = Template("{% load admin_urls %}{% edit_list profile %}")
        context = Context({"profile": Mybio.objects.get(id=1)})
        rendered = template.render(context)
        self.ok_(rendered.find("/admin/mydata/mybio/1") >= 0)


class TestCommands(DatabaseTestCase):
    """Methods for testing commands"""
    def test_models_stat_command(self):
        '''
        Test if command 'model_stats' outputs models statistics
        '''
        import sys
        from django.core.management import call_command
        from StringIO import StringIO
        real_stdout = sys.stdout
        try:
            sys.stdout = StringIO()
            call_command("model_stats")
            sys.stdout.pos = 0
            buf = "\n".join(sys.stdout.readlines())
            self.ok_(buf.find("mydata.mybio") >= 0,
                     "Model 'Mybio' not found in command output")
        finally:
            sys.stdout = real_stdout
