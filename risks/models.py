from django.db import models
from authentication.models import Account

class Risk(models.Model):
    user = models.ForeignKey(Account) # Many-to-one relationship
    code = models.IntegerField(default=0) # Lookup in the ROD table -- @todo change to ForeignKey
    duration = models.FloatField(blank=False,default=15)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.content