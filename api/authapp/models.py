from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import datetime

from django.core.cache import cache


class User(AbstractUser):
    email = models.EmailField(verbose_name='email',
                              max_length=225, unique=True)
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email

    def last_seen(self):
        return cache.get('last_seen_%s' % self.user.username)

    def online(self):
        if self.last_seen():
            now = datetime.datetime.now()
            if now > (self.last_seen() + datetime.timedelta(seconds=settings.USER_ONLINE_TIMEOUT)):
                return False
            else:
                return True
        else:
            return False
