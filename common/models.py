from django.db import models
from django.utils.translation import gettext_lazy as _

class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created time:"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated time"))

    class Meta:
        abstract = True
