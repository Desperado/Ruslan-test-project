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
        
class TestContactsForm(HttpTestCase):
    def test_contact_edit_form(self):
        '''
        Test contact edit form
        '''
        self.login(test_account["username"],
                 test_account["password"], '/accounts/login') 

        self.fv("1", "bio", "Who was born January 27?")
        self.fv("1", "first_name", "First Name")
        self.fv("1", "last_name", "Last Name")
        self.fv("1", "contacts", "0987717059, Lviv")
        self.submit(1)
        self.find("Who was born January 27?")
        self.find("First Name")
        self.find("Last Name")
        self.find("0987717059, Lviv")
        

