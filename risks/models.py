from django.db import models
import uuid
from authentication.models import Account

class Risk(models.Model):
    user = models.ForeignKey(Account) # Many-to-one relationship

    code = models.IntegerField(default=0) # Lookup in the ROD table -- @todo change to ForeignKey
    duration = models.IntegerField(blank=False,default=15) # Number of minutes
    rating = models.IntegerField(default=0) # Risk value (percentage of death)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.content