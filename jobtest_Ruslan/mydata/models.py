from django.db import models

class Mybio(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    bio = models.CharField(max_length=200)
    contacts = models.CharField(max_length=50)

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)


