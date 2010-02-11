from tddspry.django import DatabaseTestCase

from models import Mybio


test_contact = {"bio": "I was born January 27, 1984, Aquarius, like music, mountain bike and snowboard...",
                "first_name":"Ruslan",
                "last_name":"Strazhnyk",
                "contacts": "0632311999, Lviv"}
 

class TestFixture(DatabaseTestCase):
    def test_my_contact_exists(self):
        self.assert_count(Mybio, 1)
        self.assert_read(Mybio, **test_contact)



   


