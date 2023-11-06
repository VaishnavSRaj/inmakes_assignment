from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_User(self, username, password=None):
     if not username:
        raise ValueError('user must have an username')
     user=self.model(
         username=username
     )
     user.set_password(password)
     user.save(using=self._db)
     return  user

class CustomUser(AbstractUser):

    username=models.CharField(max_length=50, unique=True)
