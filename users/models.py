# users/models.py
from django_mysql.models import ListCharField

from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    blocks = ListCharField(
        base_field=models.CharField(max_length=3),
        size=50,
        max_length=(50 * 3 * 10),
        blank = True
    )
    links = ListCharField(
        base_field=models.CharField(max_length=3),
        size=150,
        max_length=(150 * 3 * 10),
        blank = True
    )

    def __str__(self):
        return self.username
