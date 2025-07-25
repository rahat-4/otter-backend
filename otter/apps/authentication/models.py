from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

import pytz
from django_countries.fields import CountryField

from common.models import BaseModel

from .choices import UserStatus, UserType
from .country_timezone import COUNTRY_TIMEZONE_MAP
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    country = CountryField(blank=True, null=True)
    time_zone = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        choices=[(tz, tz) for tz in pytz.common_timezones],
        help_text="Auto-populated based on country",
    )
    status = models.CharField(
        max_length=10,
        choices=UserStatus.choices,
        default=UserStatus.ACTIVE,
    )
    user_type = models.CharField(
        max_length=20,
        choices=UserType.choices,
        default=UserType.OWNER,
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        if self.country and not self.time_zone:
            self.time_zone = COUNTRY_TIMEZONE_MAP.get(str(self.country).upper())

        super().save(*args, **kwargs)

    @property
    def user_timezone(self):
        """Get timezone object for this user"""
        if self.time_zone:
            try:
                return pytz.timezone(self.time_zone)
            except pytz.exceptions.UnknownTimeZoneError:
                pass

        return pytz.UTC

    def __str__(self):
        return f"UID: {self.uid} | Email: {self.email}"
