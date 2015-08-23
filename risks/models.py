from django.db import models
from authentication.models import Account

class Risk(models.Model):
    user = models.ForeignKey(Account) # Many-to-one relationship
    code = models.IntegerField(default=0)
    duration = models.FloatField(blank=False,default=15)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __init__(self, user, code):
        self.user = user
        self.code = code
        self.duration = duration

    def __unicode__(self):
        return '{0}'.format(self.content)