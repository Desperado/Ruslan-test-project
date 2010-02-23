from django.db import models
from fields import PickleField
class RequestLog(models.Model):
    """Request Log Model
    """ 
    time = models.DateTimeField(auto_now_add=True)
    path = models.CharField(max_length=512, blank=True, null=True)
    method = models.CharField(max_length=512, blank=True, null=True)
    encoding = models.CharField(max_length=512, blank=True, null=True)
    view = models.CharField(max_length=512, blank=True, null=True)
    view_kwargs = PickleField(blank=True, null=True)
    view_args = PickleField(blank=True, null=True)
    get = PickleField(blank=True, null=True)
    post = PickleField(blank=True, null=True)
    meta = PickleField(blank=True, null=True)
    cookies = PickleField(blank=True, null=True)
    files = PickleField(blank=True, null=True)
    response_status = models.IntegerField(blank=True, null=True)

