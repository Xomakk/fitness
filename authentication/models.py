import uuid

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models

from authentication.manager import UserManager


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, unique=True, db_index=True, default=uuid.uuid4)
    username = None
    email = models.EmailField(unique=True, db_index=True)
    email_verfield = models.BooleanField(default=False)

    is_admin = models.BooleanField(default=True)
    created_by = models.ForeignKey('CustomUser',
                                   null=True, blank=True,
                                   on_delete=models.CASCADE,
                                   related_name="custom_users")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
