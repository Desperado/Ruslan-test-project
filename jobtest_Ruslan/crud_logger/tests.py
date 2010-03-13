from datetime import date
from tddspry.django import DatabaseTestCase
from jobtest_Ruslan.mydata.models import Mybio
from models import CRUDlogger
 
class TestCRUDLog(DatabaseTestCase):
    def test_create_logging(self):
        '''
        Test logging of model instance creation
        '''
        profile = Mybio.objects.create(first_name="test_Firstname",
                               last_name="test_Lastname",
                               date_of_birth=date(1984,01,27))
        crud_count = CRUDlogger.objects.filter(app_label=profile._meta.app_label,
                                            module_name=profile._meta.module_name,
                                            optype=CRUDlogger.OPTYPE.CREATE)\
                                    .count()
        self.ok_(crud_count == 2)
 
    def test_update_logging(self):
        '''
        Test logging of model instance update
        '''
        profile = Mybio.objects.get(id=1)
        profile.first_name = "Kurt Cobain"
        profile.save()
        crud_count = CRUDlogger.objects.filter(app_label=profile._meta.app_label,
                                            module_name=profile._meta.module_name,
                                            optype=CRUDlogger.OPTYPE.UPDATE)\
                                    .count()
        self.ok_(crud_count == 1)
 
    def test_delete_logging(self):
        '''
        Test logging of model instance delete
        '''
        profile = Mybio.objects.get(id=1)
        profile.delete()
        crud_count = CRUDlogger.objects.filter(app_label=profile._meta.app_label,
                                            module_name=profile._meta.module_name,
                                            optype=CRUDlogger.OPTYPE.DELETE)\
                                    .count()
        self.ok_(crud_count == 1)
