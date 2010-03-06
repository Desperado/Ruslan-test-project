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
                   test_account["password"], 'accounts/profile')   
        self.find(test_contact["bio"])
        self.find(test_contact["first_name"])
        self.find(test_contact["last_name"])
        self.find(test_contact["contacts"])

    def test_calendar_widget_present(self):
        """
        Test if calendar widget is loaded
        """
        self.go('accounts/profile')  
        self.find("/media/css/calendar/jscal2.css")
        self.find("/media/css/calendar/border-radius.css")
        self.find("/media/css/calendar/win2k/win2k.css")
        self.find("/media/js/calendar/jscal2.js")
        self.find("/media/js/calendar/lang/ua.js")

    def test_calendar_logo_present(self):
        """
        Test if calendar logo is loaded
        """
        self.go('accounts/profile')
        self.find("/media/admin/img/icon_calendar.gif")
        
