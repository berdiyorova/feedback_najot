from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import AbstractBaseModel


class CustomUserModel(AbstractUser, AbstractBaseModel):
    organization = models.CharField(max_length=255, verbose_name=_("Organization"))
    location = models.CharField(max_length=255, verbose_name=_("Location"))
    linkedin = models.URLField(max_length=255, verbose_name=_("linkedin"))

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
