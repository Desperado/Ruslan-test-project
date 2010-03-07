from tddspry.django import DatabaseTestCase, HttpTestCase
from models import RequestLog


class TestRequestLog(DatabaseTestCase, HttpTestCase):
    def test_count_logs(self):
        """Go for two URL's and count request logs"""
        #self.go("/something")
        #self.go("/nonsence_url")

        #self.assert_count(RequestLog,2)        
        pass


