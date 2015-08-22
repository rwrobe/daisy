from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from geoposition.fields import GeopositionField
from django.utils.translation import ugettext as _

class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError(_('Please use a valid email address')) # Internationalize the string

        if not kwargs.get('username'):
            raise ValueError(_('Please use a valid username')) # Internationalized error

        account = self.model(
            email=self.normalize_email(email),username=kwargs.get('username')
        )

        account.set_password(password) # handles salting and hashing
        account.save()

        return account

    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email, password, **kwargs) # Password is not optional

        account.is_admin=True # Other big difference, set admin flag to true
        account.save()

        return account

    def create_super_user(self):
        pass

# Extend AbstractBaseUser to add location field and allow users to login with an email address instead of just a username.
class Account(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20,unique=True)

    first_name = models.CharField(max_length=20,blank=True)
    last_name = models.CharField(max_length=40,blank=True)
    location = GeopositionField()

    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add updates once only
    updated_at = models.DateTimeField(auto_now=True) # auto_now updates everytime

    is_admin = models.BooleanField(default=False) # need this to configure the odds per category

    objects = AccountManager()

    USERNAME_FIELD = 'email' # tell Django how to authenticate (spoiler: email)
    REQUIRED_FIELDS = ['username'] # dict for required fields

    # Return email address in a readable format
    def __unicode__(self):
        return self.email

    # Return the concatenated name, e.g., John Doe
    def get_full_name(self):
        ' '.join([self.first_name, self.last_name]) # Hell yeah, string manipulation

    # Short name will just be their first name
    def get_short_name(self):
        return self.first_name
