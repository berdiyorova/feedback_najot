from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import AbstractBaseModel
from users.models import CustomUserModel

class EmployeeModel(CustomUserModel):
    position = models.CharField(max_length=255, verbose_name=_("Position of employee"))
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Employee")
        verbose_name_plural = _("Employees")
