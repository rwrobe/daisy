from django.db import models
import uuid
from authentication.models import Account

class Risk(models.Model):
    user = models.ForeignKey(Account) # Many-to-one relationship

    code = models.IntegerField(default=0) # Hard coded in Angular controllers :(
    duration = models.IntegerField(blank=False,default=15) # Number of minutes

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return ' '.join([str(self.code), str(self.duration)])