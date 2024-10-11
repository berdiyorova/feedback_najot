from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import AbstractBaseModel


class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        """Creates and returns a user with an email, password and extra fields."""
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        """Creates and returns a superuser with an email, password and extra fields."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username=username, email=email, password=password, **extra_fields)

class CustomUserModel(AbstractUser, AbstractBaseModel):
    organization = models.CharField(max_length=255, verbose_name=_("Organization"))
    location = models.CharField(max_length=255, verbose_name=_("Location"))
    linkedin = models.URLField(max_length=255, verbose_name=_("linkedin"))
    photo = models.ImageField(upload_to="users/", default="user_default_photo.png")

    objects = MyUserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
