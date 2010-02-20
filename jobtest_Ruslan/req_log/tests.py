from tddspry.django import DatabaseTestCase, HttpTestCase
from django.contrib.auth.models import User
from models import RequestLog
from jobtest_Ruslan.test_settings import test_account, test_contact


class TestRequestLog(DatabaseTestCase, HttpTestCase):
    def test_get_log(self):
        self.login(test_account["username"],
                   test_account["password"], 'accounts/profile')
        self.assert_count(RequestLog,1)        
        


