from tddspry.django import DatabaseTestCase, HttpTestCase
from django.contrib.auth.models import User
from models import Mybio
from jobtest_Ruslan.test_settings import test_account, test_contact


class TestFixture(DatabaseTestCase):
    def test_my_contact_exists(self):
        """
        Test if data is uploaded from fixture
        """
        self.assert_count(Mybio, 1)
        self.assert_read(Mybio, **test_contact)

class TestContactsViews(HttpTestCase):
    def test_contacts_view(self):
        """
        Test if contact view contains all relevant data from fixture
        """
        self.login(test_account["username"],
                  test_account["password"], 'accounts/login/?next=/accounts/profile/')   
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
                  test_account["password"], 'accounts/login/?next=/accounts/profile/')
        self.find("/media/css/calendar/jscal2.css")
        self.find("/media/css/calendar/border-radius.css")
        self.find("/media/css/calendar/win2k/win2k.css")
        self.find("/media/js/calendar/jscal2.js")
        self.find("/media/js/calendar/lang/ua.js")
        self.go('accounts/logout')


    def test_calendar_logo_present(self):
        """
        Test if calendar logo is loaded
        """
        self.login(test_account["username"],
                  test_account["password"], 'accounts/login/?next=/accounts/profile/')      
        
        self.find("/media/admin/img/icon_calendar.gif")

class TestContactsForm(HttpTestCase):
    def test_contact_edit_form(self):
        '''
        Test contact edit form
        '''
        self.login(test_account["username"],
                  test_account["password"], 'accounts/login/?next=/accounts/profile/')  
        self.fv("1", "bio", "Who was born January 27?")
        self.fv("1", "first_name", "First Name")
        self.fv("1", "last_name", "Last Name")
        self.fv("1", "contacts", "0987717059, Lviv")
        self.submit(1)
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
                model = Profile
        reversed = TestFormReverse().fields.keys()
        reversed.reverse()
        self.ok_(TestFormReverse(reverse = True).fields.keys() == reversed)

class TestTemplatetags(HttpTestCase):
    def test_edit_list_tag(self):
        '''
        Test 'edit_list' tag
        '''
        from django.template import Context, Template
        template = Template("{% load admin_urls %}{% edit_list profile %}")
        c = Context({"profile":Mybio.objects.get(id=1)})
        rendered = template.render(c)
        self.ok_(rendered.find("/admin/mydata/mybio/1") >= 0)


class TestCommands(DatabaseTestCase):
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


