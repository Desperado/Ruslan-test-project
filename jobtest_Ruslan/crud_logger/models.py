from django.db import models
from django.utils.translation import ugettext as _
 
 
class CRUDlogger(models.Model):
    class OPTYPE:
        CREATE = "create"
        UPDATE = "update"
        DELETE = "delete"

        CHOICES = (
                   (CREATE,_("Create")),
                   (UPDATE,_("Update")),
                   (DELETE,_("Delete")),
                  )

        
    
    app_label = models.CharField(max_length=512)
    module_name = models.CharField(max_length=512)
    optype = models.CharField(max_length=32,
                              choices=OPTYPE.CHOICES)
    
 
def log_save(sender, *args, **kwargs):
    if sender == CRUDlogger:
        return
    logdict = {"app_label":sender._meta.app_label,
               "module_name":sender._meta.module_name,}
    if kwargs["created"]:
        logdict.update({"optype":CRUDlogger.OPTYPE.CREATE})
    else:
        logdict.update({"optype":CRUDlogger.OPTYPE.UPDATE})
    
    CRUDlogger.objects.create(**logdict)
def log_delete(sender, *args, **kwargs):
    if sender == CRUDlogger:
        return
    CRUDlogger.objects.create(app_label=sender._meta.app_label,
                           module_name=sender._meta.module_name,
                           optype=CRUDlogger.OPTYPE.DELETE)
    
models.signals.post_save.connect(log_save)
models.signals.post_delete.connect(log_delete)
