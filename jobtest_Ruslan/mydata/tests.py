from tddspry.django import DatabaseTestCase, HttpTestCase
from django.contrib.auth.models import User
from models import Mybio
test_account = {"username":"baby",
                "password":"77722255"}


test_contact = {"bio": "I was born January 27, 1984, Aquarius, like music, mountain bike and snowboard...",
                "first_name":"Ruslan",
                "last_name":"Strazhnyk",
                "contacts": "0632311999, Lviv"}


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

        #self.go("accounts/login", kwargs=test_contact)    
        self.find(test_contact["bio"])
        self.find(test_contact["first_name"])
        self.find(test_contact["last_name"])
        self.find(test_contact["contacts"])
